from functools import reduce

prices=[100,200,300,400]

result=0
def sumof(a,b):
    return a+b
    

#total = reduce(lambda a,b:a+b,prices)
total = reduce(sumof,prices)

print(total)