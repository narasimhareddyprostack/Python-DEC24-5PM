#read emp.csv file
import csv 
fp1 = open('emp.csv','r')
data=csv.reader(fp1)
print(list(data))
print(type(list(data)))
