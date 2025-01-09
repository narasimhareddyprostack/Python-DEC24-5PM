from pymongo import MongoClient
#establish connection
client=MongoClient('mongodb://localhost:27017/')
db=client['6PM']
user_col=db['users']

female_users=user_col.find({'gender':'Male'})

for user in female_users:
    print(user['uid'], user['uname'],user['gender'])