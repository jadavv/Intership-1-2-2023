#Add data to tuple from user and print it


user = []

for i in range (int(input("Enter a nth number you want to store : "))):
    rollNo = input("Enter the number : ")
    name = input("Enter name : ")
    user.append((rollNo,name))
print(tuple(user))


