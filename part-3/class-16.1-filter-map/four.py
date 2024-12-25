numbers=[10,78,14,96,117,11,31,42]

def check(num):
    return num%2 ==0
    
even_numbres=list(filter(check,numbers))
print(even_numbres)