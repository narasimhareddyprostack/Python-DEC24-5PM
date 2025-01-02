#read emp.json file and write data into emp.csv file
import csv
import json 
fp1 = open('emp.json','r')
fp2 = open('emp.csv','w',newline="")
employees=json.load(fp1)

employees_list=[]

for emp in employees:
    #employees_list.append(list())
    employees_list.append([emp['eid'],emp['ename'],emp['gender']])

csvwrite=csv.writer(fp2)
csvwrite.writerow(['eid','ename','gender'])
csvwrite.writerows(employees_list)
fp1.close()
fp2.close()