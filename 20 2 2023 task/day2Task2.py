5#LCM Logic

num1=int(input("Enter a number 1:->"))
num2=int(input("Enter a number 2:->"))
lcm=0
if num1>num2:
    grater=num1
elif num2>num1:
    greater=num2
while True:
    if(greater%num1==0 and greater%num2==0):
        lcm=greater
        break
    greater+=1
print(lcm)