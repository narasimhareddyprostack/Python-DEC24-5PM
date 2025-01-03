class Employee:
    ''' created by Narasimha '''
    c=100

    def m1(self):
        self.a=100
    def m2(self):
        self.b=200

e1=Employee()
e1.m1()
e1.m2()
e2=Employee()
e2.m2()
print(e1.__dict__)
print(e2.__dict__)
print(Employee.__dict__)