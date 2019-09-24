'''
after
'''
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField 
from wtforms.validators import Required
'''
after
'''
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap

app = Flask(__name__) 

######
app.config['SECRET_KEY'] = 'hard to guess string'
######

bootstrap = Bootstrap(app) 

######
class NameForm(FlaskForm):    
    name = StringField('What is your name?', validators=[Required()])    
    submit = SubmitField('Submit') 
######

@app.route('/', methods=['GET', 'POST']) 
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form = form, name = session.get('name')) 



@app.route('/user/<name>') 
def user(name):    
    return render_template('user.html', name=name)

if __name__ == '__main__':    
    app.run(debug=True, host='0.0.0.0')
