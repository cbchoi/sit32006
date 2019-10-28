from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# 20191028
from . import login_manager, db

class User(UserMixin, object):
	id = ""
	#email = "cbchoi@handong.edu"
	username = "cbchoi"
	role_id = ""
	password_hash = ""

	def __init__(self, email, username, password):
		self.id = email
		self.username = username
		self.password = password
		 
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
		collection = db.get_collection('users')
		results = collection.find_one({'id':user_id})
		if results is not None:
			user = User("", "", "") #User.query.filter_by(email=form.email.data).first()
			user.from_dict(results)
			return user
		else:
			return None

# 20191028
	def to_dict(self):
		dict_user = {
			'id': self.id, 
			'username':self.username,
			#'email':self.email,
			'role_id':self.role_id,
			'password_hash':self.password_hash
		}
		return dict_user

	def from_dict(self, data):
		if data is not None:
			self.id = data['id']
			self.username = data['username']
			self.role_id = data['role_id']
			self.password_hash = data['password_hash']