fp=open('data.txt','r+')
print("Before closing")
print(fp.closed)   #False
fp.close()
print("After closing")
print(fp.closed)  #True