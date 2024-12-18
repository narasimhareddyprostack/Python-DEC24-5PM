employee={
    'eid':101,
    'ename':'Rahul',
    'esal':45000,
    'eloc':['Wayanad',"New Delhi","Noida"],
    'address':{
        'city':'Bangalore',
        'Pincode':560037
    }
}

print(employee.keys())

for key in employee.keys():
    print(key)