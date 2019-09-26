from datetime import datetime
from bson.json_util import dumps
from flask import jsonify, request, session
from pymongo import errors as db_errors

from Util import hash_password, verify_password
from App import app, mongo

from Environment_Vars import *
from Error_Codes import *

"""End Point To Add A New USer"""
@app.route('/user/add', methods=['POST'])
def add_user(): 
	
    #Reading the sent values
    try:
        request_vals = request.json
        user_name = request_vals['user_name']
        password = request_vals['password']	
    except KeyError:
        return key_error()
    except TypeError:
        return wrong_request_format_error()
    except:
        return payload_format_error()
	
    # Check the format of the sent parameters are in correct format
    if user_name and password:
        
        try :
            #Check whether the username is already existing
            if (mongo.db.user.find_one({'name': user_name})) == None:
                #Generating the password time stamp
                date_time_stamp = datetime.now()
                date_time_stamp_string = date_time_stamp.strftime("%d/%m/%Y %H:%M:%S")			

                #Hasing the password
                hashed_password = hash_password(password)

                #Adding the details to the DB		
                id = mongo.db.user.insert_one({'name': user_name, 'pwd': hashed_password, 'pwdtimestamp': date_time_stamp_string})

                #Generating the success response & sending it
                resp = jsonify('Added User ' + user_name)
                resp.status_code = 200
                return resp
            else:
                return existing_user_error()

        except db_errors.PyMongoError:
            return database_connection_error()

    else:		
        return wrong_format_error()

"""End Point To Login"""
@app.route('/login', methods=['POST'])
def login ():

    #Reading the sent values
    try:		
        request_vals = request.json
        user_name = request_vals['user_name']
        password = request_vals['password']
    except KeyError:
        return key_error()
    except TypeError:
        return wrong_request_format_error()
    except:
        return payload_format_error()

    # Check the format of the sent parameters are in correct format
    if user_name and password :
        
        try: 
            #Check whether the username is existing
            record = mongo.db.user.find_one({'name': user_name})

            if not record == None:
                saved_password = record ['pwd']

                #Checking whether the existing password and sent password are matching			
                if (verify_password (saved_password, password)):

                    #Reading the time stamp of the sent password 
                    date_time= datetime.now()
                    passwd_time_stamp = record ['pwdtimestamp']
                    passwd_time = datetime.strptime(passwd_time_stamp, '%d/%m/%Y %H:%M:%S')

                    #Checking whether the password had expired		
                    if (date_time - passwd_time).seconds > PASSWORD_EXPIRY_TIME :
                        #Setting the session to authorize the access of update endpoint
                        session[user_name] = 'SET'
                        session[user_name] = saved_password
                        return change_password ()
                    else:
                        #Generating the login success response and sending it
                        resp = jsonify('User ' + user_name + ' logged in')
                        resp.status_code = 200
                        #session[user_name] = 'SET'
                        return resp
                else: 
                    return wrong_password()
            else:
                return wrong_username()	

        except db_errors.PyMongoError:
            return database_connection_error() 			
    else:		
        return wrong_format_error()


"""End Point To Update User Details"""
@app.route('/user/update', methods=['POST'])
def update_user():

    #reading the sent values
    try:	
        request_vals = request.json
        user_name = request_vals['user_name']
        existing_password = request_vals['password']
        new_password = request_vals['newpassword']
    except KeyError:
        return key_error()
    except TypeError:
        return wrong_request_format_error()
    except:
        return payload_format_error()

     # Check the format of the sent parameters are in correct format
    if user_name and existing_password and new_password:

        try:
            #Check whether the username is correct.
            #This if condition is written because even if the session is set for user_name mistakes can happen in sending the user_name again
          
            record = mongo.db.user.find_one({'name': user_name})

            if record == None:
                return wrong_username()

            #Checking authorization to access this service. Authorization is given to user who have session set.
            if user_name in session:
			
                #Reading the existing password from the session
                exst_password = record ['pwd']
		
                #Checking whether the existing password and sent password are matching
                if (verify_password (exst_password, existing_password)):

                    #Generating the has for the new password
                    hashed_password = hash_password(new_password)

                    #Generating the time stamp for the new password
                    date_time_stamp = datetime.now()
                    date_time_stamp_string = date_time_stamp.strftime("%d/%m/%Y %H:%M:%S")
					
                    try:
                        #Updating the user details
                        mongo.db.user.update_one({'name':user_name}, {'$set': {'pwd': hashed_password, \
                                                                         'pwdtimestamp': date_time_stamp_string}})

                        #Generating the success message
                        resp = jsonify('User details updated')
                        resp.status_code = 200

                        #Dropping the session for this user
                        session.pop(user_name,None)

                        #Sending the response
                        return resp
                    except db_errors.PyMongoError:
                        return database_connection_error()
 
                else:
                    return wrong_password()	
            else:
                return access_not_allowed()
        except db_errors.PyMongoError:
            return database_connection_error() 
    else:
        return wrong_format_error()

if __name__ == "__main__":
    app.debug = True
    app.run(host=SERVER_ADDRESS, port=SERVER_PORT)
    app.run(debug = True)
