num1=int(input("Enter a number 1:->"))
num2=int(input("Enter a number 2:->"))
lcm=0
if num1>num2:
    grater=num1
elif num2>num1:
    grater=num2
while True:
    if(grater%num1==0 and grater%num2==0):
        lcm=grater
        break
    grater+=1
print(lcm)