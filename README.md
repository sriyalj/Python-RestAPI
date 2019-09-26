This work consists of two parts.
1. Python REST service API
2. Java Script file which utilizes Fetch API to consume the service end points.

### Python REST service API
This REST API is written using flask as the web server, Mongodb as the persistent storage and pymongo as the MongoDB driver. Please read the **Requirements.txt** to get further details about the exact versions used.

The following files are part of the REST API
1. Main.py - Contains the main method for the API start and service end points
2. App.py - Sets up the flask app and connection to Mongodb server and database
3. Util.py - Contains the password hashing and password matching functions
4. Environment_Vars.py - Contains the flask server and Mongodb server addresses and ports. These values are set to respective default values but can be changed according to the local machine. Additionally this file contains the flask app secret key.
5. Error_Codes.py - Contains the error messages and codes 
6. SecretKey_Gen.py - Generates a secret key for flask app.

Currently the API can ONLY process **JSON** payloads. As a result the service won't support other payload types. 

#### Service endpoints

1. Add user end point - This end point is used to register a new user. User name is taken as the primary key of a record and As a result an existing user name can't be used for another user registion
```
  ex:
      Service URL: 
                   http://localhost:5000/user/add 
      Payload:
                   {
                    "user_name": "Sriyal",
                    "password": "Sri_123"
                   }
```
2. Login end point - End point to login to the service
```
   ex:
      Service URL: 
                   http://localhost:5000/login
      Payload:
                   {
                    "user_name": "Sriyal",
                    "password": "Sri_123"
                   }
```
                   
3. Update user details - End point to update the new password 
```
  ex:
      Service URL: 
                   http://localhost:5000/user/update
      Payload:
                   {
                    "user_name": "Sriyal",
                    "password": "Sri_123",
                    "newpassword: "Sri_456"
                   }
```
### Java Script file which utilizes Fetch API
**FetchJS.js** contains Java Script Fetch API calls to the above 3 services and the response from the API calls are printed out to the console.

This Java script code was tested on NodeJS platform. Since NodeJS doesn't support fetch function node-fetch library is used.
