from pymongo import MongoClient
#establish connection
client=MongoClient('mongodb://localhost:27017/')
db=client['6PM']
user_col=db['users']

users=user_col.find()

for user in users:
    print(user['uid'], user['uname'],user['gender'])