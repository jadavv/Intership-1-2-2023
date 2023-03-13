# find palindrome name list number  count
#value=int(input("Enter the letter :"))
value =["ajaa","kataka","nayan","abcba","pratik","kataka"]
new=0
for i in value:
    if i ==i[::-1]:
        new.append(value)
print(f"total palindrone name is {new}")

