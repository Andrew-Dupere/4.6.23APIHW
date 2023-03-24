from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin

from random import randint

class User(db.Model, UserMixin): #there are multiple parent classes that the user class inherits and allows calling attributes for both
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable = False) #meaning not null
    last_name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(75), nullable = False)
    username = db.Column(db.String(75), nullable = False)
    password = db.Column(db.String(256), nullable = False)
    date_created = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    posts = db.relationship('Post', backref = 'author')


    def __init__(self,**kwargs):
        super().__init__(**kwargs) #regardless of how many arguments are passed in, find the "password=" arg
        self.password = generate_password_hash(kwargs.get('password'))
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"User {self.id}:{self.username}"
    
    def check_password(self,password_guess):
        return check_password_hash(self.password, password_guess)
    

@login.user_loader
def get_a_user_by_id(user_id):
    return db.session.get(User, user_id)

def random_photo():
    return f"https://picsum.photos/500?random={randint(1,100)}"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)
    body = db.Column(db.String, nullable = False)
    image_url = db.Column(db.String(100), nullable= False, default=random_photo)
    date_created = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id')) #SQL - foreign_key(user_id) references user(id)

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"post {self.id}{self.title}"
