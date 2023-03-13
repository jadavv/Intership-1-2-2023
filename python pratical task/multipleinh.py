
# python multiple inheritance 

class Pratik:
    Back="Oracle DB & java"
    def Backend(self):
        print("   Pratik : Backend Task implemented using :", self.Back)
class Ajay:
    Front="HTML CSS Javascript "
    def Frontend(self):
        print(" Ajay : Frontend Task Implemented  using :",self.Front)
class TeamLead(Pratik,Ajay):
    def Show(self):
        print("Dynamic website Created ..................")
        
vns=TeamLead()
vns.Backend()
vns.Frontend()
vns.Show()
