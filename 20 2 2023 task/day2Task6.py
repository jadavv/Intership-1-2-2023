#Reverse a number

num=int(input("Please Enter a Valid Number"))
reversed_num=0
while (num!=0):
    digit=num%10
    reversed_num=reversed_num*10+digit
    num//=10
print("Reveresed Number:"+str(reversed_num))