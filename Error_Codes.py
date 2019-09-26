from flask import jsonify
from App import app

@app.errorhandler(400)
def wrong_format_error(error=None):
    message = {
        'status': 400,
        'message': 'Empty user name and/or password provided',
    }
    resp = jsonify(message)
    resp.status_code = 400
    return resp

@app.errorhandler(400)
def wrong_request_format_error(error=None):
    message = {
        'status': 400,
        'message': 'Wrong data format. Data is required in JSON format ',
    }
    resp = jsonify(message)
    resp.status_code = 400
    return resp


@app.errorhandler(400)
def key_error(error=None):
    message = {
        'status': 400,
        'message': 'Wrong JSON key used ',
    }
    resp = jsonify(message)
    resp.status_code = 400
    return resp

@app.errorhandler(400)
def payload_format_error(error=None):
    message = {
        'status': 400,
        'message': 'Payload incorrectly formatted',
    }
    resp = jsonify(message)
    resp.status_code = 400
    return resp

@app.errorhandler(401)
def existing_user_error(error=None):
    message = {
        'status': 401,
        'message': 'User name already exists ',
    }
    resp = jsonify(message)
    resp.status_code = 401
    return resp

@app.errorhandler(401)
def wrong_password(error=None):
    message = {
        'status': 401,
        'message': 'Wrong password provided',
    }
    resp = jsonify(message)
    resp.status_code = 401
    return resp

@app.errorhandler(401)
def wrong_username(error=None):
    message = {
        'status': 401,
        'message': 'Wrong username provided',
    }
    resp = jsonify(message)
    resp.status_code = 401
    return resp

@app.errorhandler(401)
def change_password (error=None):

    message = {
        'status': 401,
        'message': 'Please provide new password. Use /user/update to change the password ',
    }
    resp = jsonify(message)
    resp.status_code = 401
    return resp

@app.errorhandler(403)
def access_not_allowed (error=None):

    message = {
        'status': 403,
        'message': 'Not allowed to access',
    }
    resp = jsonify(message)
    resp.status_code = 403
    return resp

@app.errorhandler(500)
def database_connection_error(error=None):

    message = {
        'status': 500,
        'message': 'Databse connection error',
    }
    resp = jsonify(message)
    resp.status_code = 500
    return resp
