import datetime
now = datetime.datetime.now()
print("Current Date Is : ")
print(now.strftime("%d-%m-%y"))
print("Current Time Is : ")
print(now.strftime("%H-%M-%S"))