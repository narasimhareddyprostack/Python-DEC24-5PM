class Account:
    def deposit_amount(self,amount):
        self.acc_Bal = amount

a1=Account()
a1.deposit_amount(15000)

a2=Account()
a2.deposit_amount(20000)


print(a1.__dict__)  #{'acc_Bal': 15000}
print(a2.__dict__)  #{'acc_Bal': 20000}