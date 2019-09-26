from flask import Flask
from flask_pymongo import PyMongo

from Environment_Vars import *

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config["MONGO_URI"] = SERVER_URL + DB_NAME
mongo = PyMongo(app)
