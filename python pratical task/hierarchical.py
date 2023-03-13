class Father:
    surname= "Jadav"
    def Show(self):
        print("my Surname is",self.surname)
        
class Son1(Father):
    def Disp(self):
        print("my name is Jayesh ",self.surname)
class Son2(Father):
    def Out(self):
        print("my name is Vinesh ",self.surname)   
        
s1=Son1()
s2=Son2()

s1.Disp()
s2.Out()
   