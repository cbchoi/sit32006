from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo

from wtforms import ValidationError
from ..models import User
from .. import db

from wtforms import FileField

class ImageRegisterForm(FlaskForm):    
    file = FileField('Upload an Image file', validators=[Required()])    
    submit = SubmitField('Submit') 
