#read data.txt and write result into new file
fp1=open('data.txt','r')
data=fp1.read()

fp2=open('wish.txt','w')
fp2.write(data)
print("New File created and written success")

fp1.close()
fp2.close()