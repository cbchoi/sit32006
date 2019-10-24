from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from . import login_manager

class User(UserMixin, object):
	id = ""
	email = "cbchoi@handong.edu"
	username = "cbchoi"
	role_id = ""
	password_hash = ""
		 
	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')
	 
	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)
	
	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	@login_manager.user_loader
	def load_user(user_id):
		return User()