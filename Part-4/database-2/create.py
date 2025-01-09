from pymongo import MongoClient
#establish connection
client=MongoClient('mongodb://localhost:27017/')
db=client['6PM']
user_col=db['users']
user_col.insert_one({'uid':101,'uname':'Rahul','loc':"Wayand"})
print("Document inserted successfully")