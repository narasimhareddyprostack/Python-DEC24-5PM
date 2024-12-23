l1 = [10,20,30,40]
#index 0 1  2  3
l1.insert(1,200) 
print(l1) #[10, 200, 20, 30, 40]
l1.remove(30)
print(l1) #[10, 200, 20, 40]
l1.remove(300) #ValueError: list.remove(x): x not in list
