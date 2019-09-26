# Flask Server-----------------------------------------------------------------------------
SERVER_PORT = 5000                      # Default Flask port, can be changed
SERVER_ADDRESS = '127.0.0.1' 		# Default localhost address, can be changed

#Flask App-----------------------------------------------------------------------------
SECRET_KEY = 'xZ5citrqIr148tq4rIZsLg'   # Generated from running the SecretKey_Gen.py
PASSWORD_EXPIRY_TIME = 30	        # Password expiry time in seconds. Can be changed to test the service

#Mongo DB Connection-----------------------------------------------------------------------------
SERVER_URL = 'mongodb://localhost:27017/' # Default Mongo localhost address and port
DB_NAME = 'testdb'                        # Persistent Storage Name

