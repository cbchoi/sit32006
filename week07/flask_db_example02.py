import pickle
import pymongo

conn = pymongo.MongoClient('mongodb://db:27017')
db = conn.get_database('myapp')
collection = db.get_collection('students')

collection.remove()

data = None
with open('raw_data.pickle', 'rb') as f:
	data = pickle.load(f)

collection.insert_many(data)

query={'grade':'A'}
results = collection.find(query)
[print(x) for x in results]
