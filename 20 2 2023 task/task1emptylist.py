num1=int(input("enter the loop You want a print"))
data=[]
for i in range(num1):
    val=int(input(f"Enter a number{i+1}:-"))
    data.append(val)
print(data)
