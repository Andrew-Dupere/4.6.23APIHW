from flask import request
from . import api
from app.models import Post, User

@api.route('/')
def index():
    return 'API CALL IS HERE'

#endpoint to get all posts
@api.route('/posts', methods=["GET"])
def get_posts():
    posts = Post.query.all()
    return [post.to_dict() for post in posts]

#get a single post
@api.route('/posts/<post_id>')
def get_post(post_id):
    post = Post.query.get(post_id)
    if post is None:
        return {'error':f'Post with id {post_id} does not exist'}
    
    return post.to_dict()

#create a post
@api.route('/posts', methods=["POST"])
def create_post():
    #check to see that the request body is JSON 
    if not request.is_json:
        return {'error':'Your request content type must be application/json'}, 400
    data = request.json

    #validate data
    required_fields = ['title','body','user_id']
    for field in required_fields:
        if field not in data:
            return {'error':f"{field} must be in request body"}, 400
        
    #get data from request body

    title = data.get('title')
    body = data.get('body')
    image_url = data.get('image_url')
    user_id = data.get('user_id')

    #upon initilaization of a post class, db commit is ran
    new_post = Post(title=title, body=body, image_url=image_url, user_id=user_id)
    
    #return new post as a JSON response
    return new_post.to_dict(), 201 #201 is status code for creating

    #create get user
    #may need to create a method on the user class

@api.route('/users', methods=["GET"])
def get_users():
    users = User.query.all()
    return [user.to_dict() for user in users]



    #create create user route

@api.route('/user', methods=["POST"])
def create_user():
    #check to see that the request body is JSON 
    if not request.is_json:
        return {'error':'Your request content type must be application/json'}, 400
    data = request.json

    #validate data
    required_fields = ['first_name','last_name','email','username','password']
    for field in required_fields:
        if field not in data:
            return {'error':f"{field} must be in request body"}, 400
        
    #get data from request body

    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    #upon initilaization of a post class, db commit is ran
    new_user = User(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
    
    #return new post as a JSON response
    return new_user.to_dict(), 201 #201 is status code for creating
