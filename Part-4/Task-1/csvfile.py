import csv
import requests
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
fp = open('product.csv','w',newline='')
csvwrite=csv.writer(fp)
csvwrite.writerow(['p_Id','p_Name','price'])

for product in new_products:
    csvwrite.writerow([product['pid'],product['pname'],product['price']])

print('New CSV File Created!')