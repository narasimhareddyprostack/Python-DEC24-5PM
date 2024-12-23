numbers=[10,78,14,96,117,11,31,42]

def check(num):
    if num %2 ==0:
        return True
    else:
        return False
    

filter_obj=filter(check,numbers)
print(list(filter_obj))