# python access modifiers


class A:  # parent
    a=500  #public
    _b= 500# protected
    __c =300 # private
    print(a,"",_b,"",__c)
    
    
    
    
    def add(self):
        self.__c=self.a+self._b
        print("Addition:",self.__c)
obj=A()
obj.add()
# print(obj.a)
# print(obj._b)
# print(obj.__c)

class B:  # 
    def Show(self):
        print(A.a)
        print(A._b)
        print(A.__c)
obj=B()
obj.Show()
    
   
    
#     pass
# obj=B()
# # obj.Show()

# print(obj.a)
# print(obj._b)
# print(obj.__c)


    

