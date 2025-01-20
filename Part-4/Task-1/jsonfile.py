import requests
import json 
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

fp=open('product.json','w')
json.dump(new_products,fp)
print('New JSON File Created!')
