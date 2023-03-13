# base class

class Parent:
    def func1(self):
        print(" this funcation is  in parent class ")
# Derived class

class Child (Parent):
    def func2(self):
        print(" this function is in child class")
        
        
        
        
        
ob=Child()
ob.func1()
ob.func2()