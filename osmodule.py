import os

print("List all directory")
print(os.listdir())

print("Current Directory Path ")
print(os.getcwd())

print("Make new directory")
m=input("Enter Name for create a folder :")
os.mkdir(m)
print("FOLDER CREATED")

path=input("Enter the path exists or not :")
print(os.path.exists(path))

f=input("Enter the file exists or not")
print(os.path.isfile(f))

d=input("Enter the folder to delete :")
os.rmdir(d)
print("FOLDER DELETED")