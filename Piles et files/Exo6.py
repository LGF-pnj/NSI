class Pile_bornee :
    def __init__(self, c):
        self._contenu=[]
        self._capacite=c+1
        self._nb=0
    
    def est_vide(self):
        if self._nb != 0 :
            return False
        return True
    
    def est_pleine(self):
        if self._nb == self._capacite :
            return True
        return False
    
    def empiler(self, e):
        if self.est_pleine():
            raise IndexError("la pile est pleine")
        else :
            self._contenu.append(e)
            self._nb+=1
    
    def depiler(self):
        if self.est_vide():
            raise IndexError("la pile est vide")
        else :
            result=self._contenu.pop()
            return result


def creer_pile_bornee(c):
    return Pile_bornee(c)

p=creer_pile_bornee(4)
print(p.est_vide())
p.empiler("elem1")
p.empiler("elem2")
print(p.depiler())
p.empiler("elem2bis")
print (p.est_pleine())
p.empiler("elem3")
print(p.est_vide())
p.empiler("elem4")
print(p.est_pleine())


