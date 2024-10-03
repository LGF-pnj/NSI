class Fraction :
    """une classe permettant de représenter les nombrs rationnels"""
    def __init__(self, numeur, denomeur):
        if denomeur>0 :
            self.num=numeur
            self.denom=denomeur
        else :
            raise ValueError("Dénominateur pas strictment positif")
        
    def __str__(self):
        numeur=self.num
        denomeur=self.denom
        if denomeur==1:
            return (str(numeur))
        else :
            return (str(numeur)+"/"+str(denomeur))
    
    def __eq__(self, subject):
        return (self.num*subject.denom==self.denom*subject.num)

    def __lt__(self,subject):
        return (self.num*subject.denom<self.denom*subject.num)
    
    def __add__(self,subject):
        adder=self.num*subject.denom
        addto=subject.num*self.denom
        denomcom=self.denom*subject.denom
        result=Fraction(adder+addto, denomcom)
        return result

    def __mul__(self, subject):
        newself=Fraction(self.num*subject.num, self.denom*subject.denom)
        return newself

    def simplifie(self):
        pass

f=Fraction(2,3)
r=Fraction(2,5)

print(f+r)
