# python multilevel inheritance  

class Father:
    surname="katara"
class Son(Father):
    def Show(self):
        print("ajay",self.surname)
class Sister(Father):
    def Show2(self):
        print(" your sister :dharti",self.surname)
    
class son(Sister):
    def sp(self):
        print(" your dodar :kaybi",self.surname)
        
v=Son()
v.Show()

s=Sister()
s.Show2()

g=son()
g.sp()
    