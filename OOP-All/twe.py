class Test:

    def m1(self):
        print("Instance Method") 
    @classmethod
    def m2(cls):
        print("class method") 
    @staticmethod
    def m3():
        print("static Method")
t1 = Test()
t2 = Test()
print(Test.__dict__)
print(t1.__dict__)
print(t2.__dict__)