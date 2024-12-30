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
print(len(list(new_male_employees)))