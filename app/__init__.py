from flask import Flask


myobj = Flask(__name__)
myobj.config['SECRET_KEY'] = 'you-will-never-guess'

from app import routes
