import pymongo
conn = pymongo.MongoClient('mongodb://db:27017')
db = conn.get_database('example')
collection = db.get_collection('example')

collection.delete_many({'name':'rhchoi'})
collection.insert_one({'name':'cbchoi', 'id':2190000})

print('Find all documents which key is "cbchoi"')
results = collection.find({'name':'cbchoi'})
print((lambda x: x[0] if x.count() > 0 else 'not found')(results))

print('Update the name of the first documents to "rhchoi"')
results = collection.update_one(results[0], {'$set':{'name':'rhchoi'}})
results = collection.find({'name':'rhchoi'})
print((lambda x: x[0] if x.count() > 0 else 'not found')(results))

results = collection.find({'name':'cbchoi'})
print((lambda x: x[0] if x.count() > 0 else 'not found')(results))

