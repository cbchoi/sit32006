from wtforms import Form
from wtforms import StringField, SubmitField 
from wtforms.validators import Required

from flask import Flask 
app = Flask(__name__) 

app.config['SECRET_KEY'] = 'hard to guess string'


class NameForm(Form):    
	name = StringField('What is your name?', validators=[Required()])
	submit = SubmitField('Submit') 

if __name__ == '__main__':    
	app.run(debug=True, host='0.0.0.0')