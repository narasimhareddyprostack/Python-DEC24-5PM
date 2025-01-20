import requests
import mysql.connector

data = requests.get('https://dummyjson.com/products')
products=data.json()['products']
new_products=[]
for prod in products:
    new_products.append((prod['id'],prod['title'],prod['price'],prod['category']))

dbcon=None
cursor=None 
try:
    dbcon=mysql.connector.connect(host='localhost',user='root',password='root',database='6pm')
    cursor=dbcon.cursor()
    sql_st = '''
             insert into products(prod_Id,prod_Name,price, category) values(%s,%s,%s,%s);
             '''    
    cursor.executemany(sql_st,new_products)
    dbcon.commit()
    print('Data Inserted successfully!')
except mysql.connector.Error as err:
    print(err)
