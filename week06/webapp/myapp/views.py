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
		html_line += "<h2>"
		html_line += str(results[0]['id'])
		html_line += "</h2>\n"
		return html_line
	else:
		return '<h1> Page Not Found </h1>'	
