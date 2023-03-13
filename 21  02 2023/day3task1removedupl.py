# remove  duplicate element from list 

remove=int(input(" enter the value :"))

data=[]

for i in range(remove):
    val=str(input(f" Enter the number{i+1}:"))
    data.append(val)
print(data)
print("the original list",data)

res=[]
[res.append(x) for x in data if x not in res]


print("the list after  removing duplicate :",res)









