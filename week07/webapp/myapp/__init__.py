from flask import Flask

app = Flask(__name__, instance_relative_config=True)

def initialize_app():
	app.config.from_object('config')
	app.config.from_pyfile('config.py') 

	from . import views
	
	@app.route('/') 
	def index():    
	    return '<h1>Hello World!</h1>'

	@app.route('/user/<name>') 
	def user(name):    
	    return f'<h1>Hello, {name}!</h1>'


	return app
