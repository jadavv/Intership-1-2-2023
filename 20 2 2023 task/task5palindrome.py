num=int(input("Enter a Number"))
temp=num
rev=0
while(num>0):
    digit=num%10
    rev=rev*10+digit
    num=num//10
if(temp==rev):
    print("PAlINDROME")
else:
    print("NOT PALINDROMW")
