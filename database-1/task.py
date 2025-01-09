import requests
import pymongo

data=requests.get('https://dummyjson.com/products')
product_data=data.json()
print(type(product_data))  #dict
print(type(product_data['products'])) #list

client = pymongo.MongoClient('mongodb://localhost:27017/') 
db=client['6PM']
product_col = db['products']

product_col.insert_many(product_data['products'])
