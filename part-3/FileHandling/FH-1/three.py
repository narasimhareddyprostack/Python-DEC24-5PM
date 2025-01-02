fp=open("data.txt",'r')
data=fp.readlines()  # return all lines into list format
print(data)
fp.close()