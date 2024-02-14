l=[]
num=int(input("No.Of.Elements : "))
for i in range(num):
    val = int(input("Enter Number "+str(i+1)+" : "))
    l.append(val)
max=l[0]
for i in l:
    if(max<i):
        max = i
print("Maximum : ",max)