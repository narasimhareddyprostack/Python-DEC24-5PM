
try:
    a = int(input("Enter First Number:"))
    b = int(input("Enter Second Number:"))
    print("a Value:",a, "b Value:",b)
    fp = open("emp.json",'r')
    data=fp.read()
    print(data)

except:
    print("please check code")

except TypeError as te:
    print("Type Mismatch")

except ValueError as ve:
    print("Unable to Convert")

finally:
    print("finally Block will execute always")
    
