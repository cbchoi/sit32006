from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__) 
bootstrap = Bootstrap(app) 
moment = Moment(app)
# initialize moment on the app within create_app()
moment.init_app(app)

@app.route('/') 
def index():
	print(url_for('index'))     
	print(url_for('index', page=2))
	print(url_for('index', _external=True))          
	return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>') 
def user(name):    
	
	return render_template('user.html', name=name)

if __name__ == '__main__':    
    app.run(debug=True, host='0.0.0.0')
