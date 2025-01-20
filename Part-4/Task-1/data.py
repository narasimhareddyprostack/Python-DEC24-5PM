import requests
import mysql.connector

data = requests.get('https://dummyjson.com/products')
products=data.json()['products']
new_proudcts=[]
for prod in products:
    new_proudcts.append((prod['id'],prod['title'],prod['price'],prod['category']))
    
print(new_proudcts)