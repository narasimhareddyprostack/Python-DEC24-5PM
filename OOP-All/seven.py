a=10
ename="rahul"

def add():
    pass
class Test:
    pass 

t1= Test()
t2= Test()
print(id(a))      #140733663496920
print(id(ename))  #2856073991520
print(id(add))    #2856073991243
print(id(t1))     #4242856073991520
print(id(t2))     #28560739924324