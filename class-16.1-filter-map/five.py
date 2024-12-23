numbers=[10,78,14,96,117,11,31,42]

def check(num):
    return num%2 !=0
    
odd_numbers=list(filter(check,numbers))
print(odd_numbers)