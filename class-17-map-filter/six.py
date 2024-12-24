a=10        # global scope
def wish():
    a=100   # local scope
    b=200
    print(a) #100

wish()
print(a)  #10