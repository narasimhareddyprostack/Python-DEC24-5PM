from pymongo import MongoClient
#establish connection
client=MongoClient('mongodb://localhost:27017/')
db=client['6PM']
user_col=db['users']

#update one document
#update user name - rahul to Rahul Gandhi
status=user_col.update_one({'uid':1},{ "$set": { 'uname': 'Rahul Gandhi' } })
print(status)
print("Deleted Successfullt")