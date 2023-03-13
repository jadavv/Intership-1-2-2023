i=int(input(" enter the number to check for armstrong"))

sum=0
orig=i
while (i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if orig==sum:
    print("Armstrong")
else:
    print("not Armstrong ")
        