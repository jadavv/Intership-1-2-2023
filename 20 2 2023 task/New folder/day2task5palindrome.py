num=int(input("Enter the a number "))
temp =num 
rev=0
while (num>0):
    digit=num%10
    rev=rev*10+digit
    num=num//10
if (temp==rev):
    print("palindrome")
else:
    print(" not palindrom")
    
    
    
    
    
string = input(("Enter the a letter ")) 

print(string[::-2])  

# if (string==string[::-1]):
#     print("the letter  is a palindrome")
# else:
#     print("the letter is not a palindrome")
    