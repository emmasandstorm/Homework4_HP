from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField
from wtforms.validators import DataRequired
 

myobj = Flask(__name__)
myobj.config['SECRET_KEY'] = 'you-will-never-guess'

 
class LoginForm(FlaskForm):
    user_input = StringField('City Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

from app import routes

