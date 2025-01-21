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
            insert into employee values(101,'Rahul',45000.45);
            '''
    cursor.execute(sql_st)
    dbcon.commit()
    print('record inserted Successfully')
except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()