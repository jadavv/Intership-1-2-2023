
   # inheritance  programm

class Father:
    def Lands(self):
       print("having 5000 Ekar lands ")
    
    
class Son (Father):
    def Money(self):
        print("having 100 lakhs money ")
        
S=Son()
S.Money()
S.Lands()



# type of inheritance
  #1) singal /simple inheritance
  
  
class A:
      num1=int(input("enter the number :"))
      num2=int(" enter the number:")
      
      def Add(self):
          print("Addtion :", self.num1+ self.num2)
      def Sub(self):
          print("Subcriptipn :",self.num1-self.num2)
          
class C(A):
    def Multi(self):
        print("Multipication: ",self.num1* self.num2)
    
    def Div (self):
        print("divisation :",self.num1/self.name)
    def rem(self):
        print("modulation  :", self.num1%self.num2 )   
      
    obj =BaseException()
    obj.Add()
    obj.Sub()
    obj.Multi()
    obj.Div()
    obj.rem()
      
      
  
  

