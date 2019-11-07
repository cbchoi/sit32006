from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# 20191028
from . import login_manager, db

# 20191108
from flask import current_app, request, url_for
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer 

class User(UserMixin, object):
	id = ""
	#email = "cbchoi@handong.edu"
	username = "cbchoi"
	role_id = ""
	password_hash = ""
	confirmed = False

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

	##### 20191108
	def generate_confirmation_token(self, expiration=3600):
		s = Serializer(current_app.config['SECRET_KEY'], expiration)
		return s.dumps({'confirm': self.id}).decode('utf-8')

	def confirm(self, token):
		s = Serializer(current_app.config['SECRET_KEY'])
		try:
			data = s.loads(token.encode('utf-8'))
		except:
			return False
		if data.get('confirm') != self.id:
			return False
		self.confirmed = True
		collection = db.get_collection('users')
		results = collection.update_one({'id':self.id}, {'$set':{'confirmed':self.confirmed}})
		return True
    #####

# 20191028
	def to_dict(self):
		dict_user = {
			'id': self.id, 
			'username':self.username,
			#'email':self.email,
			'role_id':self.role_id,
			'password_hash':self.password_hash,
			'confirmed':self.confirmed
		}
		return dict_user

	def from_dict(self, data):
		if data is not None:
			self.id = data['id']
			self.username = data['username']
			self.role_id = data['role_id']
			self.password_hash = data['password_hash']
			self.confirmed =data['confirmed']