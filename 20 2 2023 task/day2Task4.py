#Fibinacci

number=int(input("Enter How many terms you want to print Fibonacci series:->"))
n1,n2=0,1
count=0
if(number<=0):
    print("Please Enter a Positive Integer")
elif(number==1):
    print("Fibonacci Series Sequence upto",number,":")
    print(n1)
else:
    print("Fibonacci Sequence")
    while(count<number):
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
        