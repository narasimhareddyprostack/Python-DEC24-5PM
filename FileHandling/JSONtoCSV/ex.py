import csv
fp = open('emp.csv','w',newline="")
csvwriter=csv.writer(fp);

emp_list=[[1,'Rahul','Male'],[2,'Sonia','Female']]
csvwriter.writerow(['eid','ename','gender'])
csvwriter.writerows(emp_list)
fp.close()