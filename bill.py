price=80
quantity=7
discount=30
tax=18
price=quantity*price
tax=(price*tax)/100
discount=(price*discount)/100
totalAmount = price - discount + tax
print("Amount : ",totalAmount)