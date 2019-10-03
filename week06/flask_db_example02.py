import pymongo
conn = pymongo.MongoClient('mongodb://db:27017')
db = conn.get_database('myapp')
collection = db.get_collection('students')

result = collection.insert_one({'name':'cbchoi', 'id':'2190000'})
print(result.inserted_id)

results = collection.find({'id':'2190000'})
[print(x) for x in results]

collection.delete_many({'name':'cbchoi', 'id':'2190000'})