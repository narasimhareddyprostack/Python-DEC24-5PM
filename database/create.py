import pymongo
#help(pymongo)

client = pymongo.MongoClient('mongodb://localhost:27017/') 
db=client['6PM']
col_name=db['users']
#write python -dict data into mongodb collection
col_name.insert_one({'eid':101,'ename':'rahul'})
print("Inserted Successfully")
