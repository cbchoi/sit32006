@app.route('/') 
def index():    
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>') 
def user(name):    
    return f'<h1>Hello, {name}!</h1>'

@app.route('/<int:id>/<int:num>') 
def userid(id, num):    
    return f'<h1>Hello, {id}!</h1>' * num