import requests
import pymongo
data = requests.get('https://dummyjson.com/products')
products=data.json()['products']

new_products=[]

for prod in products:
    new_products.append({
        'pid':prod['id'],
        'pname':prod['title'],
        'category':prod['category'],
        'price':prod['price'],
        'rating':prod['rating']
    })
try:
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db=client['6PM']
    product_col=db['products']
    product_col.insert_many(new_products)
    print('Product Data Written successfully')

except:
    pass
finally:
    pass
