var = {10,"run",345,"ankit","true",'pyhon',56.09,6.00,77,65,75}
var2 = {10,"run","gsss",345,"ankit",564,"true",5533,'pyhon',56.09,6.00}

print(var)
print(var2)
# var.update([" cool vinesh"])

# print(var.pop())


print(var.intersection(var2))
print(var & var2)

print(var.union(var2))
# print(var | var2)
print(var.difference(var2))
print(var -var2)

print(var.symmetric_difference(var2))
print(len(var))