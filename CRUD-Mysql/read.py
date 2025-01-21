import mysql.connector
dbcon=None
cursor =None 
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='jandb')
    cursor=dbcon.cursor()
    sql_st=''' 
                select * from employee;
            '''
    cursor.execute(sql_st)
    employees=cursor.fetchall()

    for emp in employees:
        print("employee Id",emp[0],"Employee Name", emp[1])

    print(employees)
    
    print('Fetching Data Successfully')
except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()