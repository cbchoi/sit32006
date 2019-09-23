<<<<<<< HEAD
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

@app.route('/<int:id>/<string:password>') 
def userid(id, password):
	user_manage = {}
	user_info = {}

	f = open('data.csv', "r")
	for line in f:
		line = line.strip()
		info = line.split(', ')
		user_manage[int(info[0])] = info[1]
		user_info[int(info[0])] = info[2:]
		#print(info)
	print(user_manage)
	print(user_info)

	if user_manage[id] == password: # authenticate logic
		html_line = f"<h1>{id}'s score </h1>\n"
		for item in user_info[id]:
			html_line += "<h2>"
			html_line += item
			html_line += "</h2>\n"

		return html_line
	else:
		return '<h1> Page Not Found </h1>'	
=======
>>>>>>> d93dd5c0edd40ee35809e6dc627e2a4ea5558d73
