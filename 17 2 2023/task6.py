salary=int(input("Enter the monthaly salary of empolyee :"))
anualsalary=salary*12
    
if anualsalary>200000:
    
    net=(anualsalary*(5/100))/12
    print("monthly net salary  of employe is ",net)
    
elif anualsalary>500000:
    net=(anualsalary*(10/100))/12
    print("monthly net salary of employede is ",net)
         
elif anualsalary>1000000:
    net=(anualsalary*(15/100))/12
    print("monthly net salary of employede is ",net)
 
elif anualsalary>1500000:
    net=(anualsalary*(20/100))/12
    print("monthly net salary of employede is ",net)
                 
    