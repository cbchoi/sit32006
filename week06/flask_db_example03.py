import pymongo
conn = pymongo.MongoClient('mongodb://db:27017')
db = conn.get_database('example')
collection = db.get_collection('example')

print('Find all documents')
results = collection.find()
[print(result) for result in results]

print('Find all documents which key is "cbchoi"')
results = collection.find({'name':'cbchoi'})
[print(result) for result in results]
