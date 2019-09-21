from flask import Flask
#from . import views

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
app.config.from_pyfile('config.py') 

@app.route('/') 
def index():    
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>') 
def user(name):    
    return f'<h1>Hello, {name}!</h1>'

user_map = {}

@app.route('/<int:id>/<string:password>') 
def userid(id, password): 
	f = open('data.csv', "r")
	for line in f:
		line = line.strip()
		user_info = line.split(',')
		print(user_info)


	return f'<h1>Hello, {id}!</h1>' * 2