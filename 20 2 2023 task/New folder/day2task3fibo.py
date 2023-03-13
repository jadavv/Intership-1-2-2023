number = int(input("Enter how many tern you want to print fibonacci series: "))
n1,n2=0,1
count =0
if (number <= 0):
    print(" Please Enter a positive integer")
elif(number ==1):
    print("Fibonacci series Sequence upto ", number ,":")
    print(n1)
else:
    print("fibonacci sequence")
    while(count<number ):
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
