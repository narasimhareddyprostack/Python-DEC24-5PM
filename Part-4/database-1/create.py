import pymongo
#help(pymongo)
# Connect to a local MongoDB instance
client = pymongo.MongoClient('mongodb://localhost:27017/') 
# Access a specific database
db=client['6PM']
# Access a collection (similar to a table in SQL databases)
col_name=db['users']
#write python -dict data into mongodb collection
# Single document
col_name.insert_one({'eid':101,'ename':'rahul'})
print("Inserted Successfully")
