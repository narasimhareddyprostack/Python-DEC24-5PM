from pymongo import MongoClient
#establish connection
client=MongoClient('mongodb://localhost:27017/')
db=client['6PM']
user_col=db['users']

#delete one document
status=user_col.delete_many({'gender':'Male'})
print(status)
print("Deleted Successfullt")
