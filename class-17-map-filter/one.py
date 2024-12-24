numbers=[10,150,230,130,30,70,500]

def check(ele):
    return ele<100

#filtered_data=filter(check,numbers)
filtered_data=filter(lambda ele:ele<100,numbers)
print(type(filtered_data))
result=list(filtered_data)
print(result)