#read emp.csv file
import csv 
fp1 = open('emp.csv','r')
csv_data=csv.reader(fp1)
users=list(csv_data)
print(users)

for user in users:
    print(user)