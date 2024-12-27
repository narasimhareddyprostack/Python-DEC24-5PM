import json 
fp=open('employees.json','r')
employees=json.load(fp)
print(type(employees))  #<class,list>
print(len(employees))   #20
#print(employees)        #[{},{}]

female_emp=[]
for emp in employees:
    if emp['gender']=='Female':
        #print(emp['ename'])
        female_emp.append(emp)

fp2=open('female.json','w')
json.dump(female_emp,fp2)

print("New File Created Successfully")