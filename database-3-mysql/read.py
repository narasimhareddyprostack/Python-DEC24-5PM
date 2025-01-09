#read mysql employee table and print employee data
import mysql.connector

db_con = mysql.connector.connect(host="localhost",user="root",password="root",database="6pm")
cursor = db_con.cursor()

cursor.execute("Select * from employees")
employees=cursor.fetchall()
print(type(employees))

for emp in employees:
    print(emp)