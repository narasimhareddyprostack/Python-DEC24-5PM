class Account:
    def __init__(self,id,name):
        self.acc_id=id
        self.acc_name=name

a1=Account(11,'Rahul')
print(a1.__dict__)
a2=Account(12,'Sonia')
print(a2.__dict__)