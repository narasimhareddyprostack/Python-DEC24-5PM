import requests

data = requests.get('https://dummyjson.com/products')
products=data.json()['products']

print(type(product_data))  #<class 'dict'>
print(type(product_data['products']))  #<class 'list'>

