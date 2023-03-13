value=int(input(" Enter the loop you want a print"))
data=[]
for j in range(value):
    val=int(input(f" Enter a number {j+1}:"))
    data.append(val)
print(data)