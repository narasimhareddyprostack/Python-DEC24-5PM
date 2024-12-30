#Read employees.csv file,
#and write male data into new json file ie male.json
import csv
import json

fp1 = open('employees.csv','r')
fp2 = open('male.json','w')
employees=list(csv.reader(fp1))
print(len(employees))

#new_male_employees=filter(fun,seq)
new_male_employees=filter(lambda emp_list:emp_list[2]=="Male",employees)
print(new_male_employees)
male_employees=[]
for emp_list in new_male_employees:
    male_employees.append({'eid':emp_list[0],'ename':emp_list[1]})

json.dump(male_employees,fp2)
print("New File Created")

fp2.close()
fp1.close()