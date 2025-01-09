class Account:
    def __init__(self,a,b,c):
        self.acc_id=a 
        self.acc_name=b 
        self.acc_bal=c

    def deposit_amount(self,amount):
        self.acc_bal = self.acc_bal+amount


a1=Account(101,'Rahul',1500)
a2=Account(102,'Sonia',5000)
print(a1.__dict__)
print(a2.__dict__)
print("After Deposit")

a1.deposit_amount(50)

a2.deposit_amount(150)

print(a1.__dict__)
print(a2.__dict__)
