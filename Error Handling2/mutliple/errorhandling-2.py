fp=None
try:
    fp=open('emp.json','r')
    data=fp.read()
    a = int(input("Enter First Number:"))
    b = int(input("Enter Second Number:"))
    print(a+b)

except ValueError as ve:
    print("Unable to Convert")

except TypeError as te:
    print("Type Mismatch")
    
except FileNotFoundError as fnf:
    print(fnf)
    fp=open("default.json",'r')
    


finally:
    print("finally Block will execute always")
    fp.close()
