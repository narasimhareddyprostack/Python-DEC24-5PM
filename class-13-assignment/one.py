customers=[
    {'cid':101,'cname':"Rahul","mobile":9591619191},
    {'cid':102,'cname':"Sonia","mobile":9490061300},
    {'cid':103,'cname':"Rahul","mobile":9591619191},
    {'cid':104,'cname':"Rahul Gandhi","mobile":9591619191},
    {'cid':105,'cname':"Sonai Gandhi","mobile":9490061300},
    {'cid':106,'cname':"Rahul Ji","mobile":9591619191},
    {'cid':107,'cname':"Priyanka","mobile":9490061300},
]
#send - christmax message to all customer's
mobile_numbers=[]
for cust in customers:
    mobile_numbers.append(cust['mobile'])

print(mobile_numbers)