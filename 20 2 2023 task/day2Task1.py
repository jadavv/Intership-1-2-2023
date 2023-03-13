num = int(input("Enter a number you want to check it is Armstrong number or not: "))

sum = 0
n = len(str(num))
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit**n
    temp //= 10
if num == sum:
    print(num,"is Armstrong number")
else:
    print(num,"is not Armstrong number")