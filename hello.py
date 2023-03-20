from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'My name is Andrew'


@app.route('/asdf')
def hello_worl():

    asdf = 213
    return asdf



