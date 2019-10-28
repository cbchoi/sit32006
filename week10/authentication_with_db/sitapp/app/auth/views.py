from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, logout_user
from ..models import User
from .forms import LoginForm, RegistrationForm
from . import auth

from .. import db

@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		collection = db.get_collection('users')
		results = collection.find_one({'id':form.email.data})
		if results is not None:
			user = User("", "", "") #User.query.filter_by(email=form.email.data).first()
			#print(form.email.data)
			user.from_dict(results)
			if user is not None and user.verify_password(form.password.data):
				login_user(user, form.remember_me.data)
				return redirect(request.args.get('next') or url_for('main.index'))
		flash('Invalid username or password.')
	return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have been logged out.')
	return redirect(url_for('main.index'))

@auth.route('/register', methods=['GET', 'POST'])
def register(): 
    form = RegistrationForm() 
    if form.validate_on_submit(): 
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        #db.session.add(user) 
        collection = db.get_collection('users')
        collection.insert_one(user.to_dict())
        flash('You can now login.') 
        return redirect(url_for('auth.login')) 
    return render_template('auth/register.html', form=form)