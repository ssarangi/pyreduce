from flask import Flask

webapp = Flask(__name__)

@webapp.route('/')
def index():
    return '<h1>Hello World</h1>'