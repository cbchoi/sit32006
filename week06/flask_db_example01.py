import pymongo
conn = pymongo.MongoClient('mongodb://db:27017')
db = conn.get_database('example')
collection = db.get_collection('example')

results = collection.find()
[print(result) for result in results]
