from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS



app = Flask(__name__)
app.config.from_object(Config)
#app is an instance of the flask app, app.config calls an attribute of the flask app

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

db = SQLAlchemy(app)

migrate = Migrate(app, db)

#create instance of login manager to set up authentication
login = LoginManager(app)

login.login_view = 'login'
login.login_message = 'You can not do that'
login.login_message_category = 'danger'


#import the api blueprint and register it with flask app
from app.blueprints.api import api
app.register_blueprint(api)


#import all of the routes from the routes file into current package

from app import routes, models
#everything in forms.py is initialized in the routes file so you only see routes and models here
