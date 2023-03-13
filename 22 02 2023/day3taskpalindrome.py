# find palindrome name list number  count
#value=int(input("Enter the letter :"))
value =["ajaa","kataka","nayan","abcba","pratik","kataka"]
count=0
for i in value:
    if count ==i[::-1]:
        count+=value
print(f"total palindrone name is {count}")