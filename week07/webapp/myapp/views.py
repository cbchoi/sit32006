from . import app

import pymongo

@app.route('/<string:_name>') 
def userid(_name):
	conn = pymongo.MongoClient('mongodb://db:27017')
	db = conn.get_database('example')
	collection = db.get_collection('example')

	results = collection.find({'name':_name})
	if results.count() > 0:
		html_line = f"<h1>{_name}'s ID </h1>\n"
		for result in results:
			html_line += "<h2>"
			if result.get('id'):
				html_line += str(result['id'])
			else:
				html_line += str(result['name'])
			html_line += "</h2>\n"
		return html_line
	else:
		return '<h1> Page Not Found </h1>'	

@app.route('/create/<string:_name>') 
def create_user(_name):
	conn = pymongo.MongoClient('mongodb://db:27017')
	db = conn.get_database('example')
	collection = db.get_collection('example')

	collection.insert_one({'name':_name})
	return f'<h1> {_name} is inserted into db</h1>'	

@app.route('/delete/<string:_name>') 
def delete_user(_name):
	conn = pymongo.MongoClient('mongodb://db:27017')
	db = conn.get_database('example')
	collection = db.get_collection('example')

	collection.delete_one({'name':_name})
	return f'<h1> {_name} is deleted from db</h1>'	
