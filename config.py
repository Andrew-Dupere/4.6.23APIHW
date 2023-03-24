import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'WelcomeToTheDesert' #the or is only for testing, not production
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABSASE_URL') or 'sqlite:///'+os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

