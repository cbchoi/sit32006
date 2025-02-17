from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Required, Email, Length

######
class NameForm(FlaskForm):    
    name = StringField('What is your name?', validators=[Required()])    
    submit = SubmitField('Submit') 
######

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[Required(), Length(1, 64),	Email()])
	password = PasswordField('Password', validators=[Required()])
	remember_me = BooleanField('Keep me logged in')
	submit = SubmitField('Log In')
