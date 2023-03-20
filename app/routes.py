from app import app

@app.route('/')
def hello_world():
    return 'My name is Andrew'


@app.route('/asdf')
def hello_worl():

    asdf = 213
    return asdf

