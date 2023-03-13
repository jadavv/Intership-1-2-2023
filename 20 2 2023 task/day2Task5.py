#Twin No.

t = int(input("Enter The Number :--"))
temp = t
string = str(t)
sum = 0
for digit in string:   
    sum += int(digit)

string = str(temp)
product = 1
for digit in string:
    product *= int (digit)

    if sum == product:
        print("Number Is Twin Number")
    else :
        print("Number IS Not Twin Number")
        