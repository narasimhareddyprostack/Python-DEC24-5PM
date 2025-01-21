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
                delete from employee;
            '''
    cursor.execute(sql_st)
    dbcon.commit()   

    print('Data Deleted Successfully')
except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()