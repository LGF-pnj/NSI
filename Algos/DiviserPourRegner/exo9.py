class Cellule:
    def __init__(self, v, s):
        self.valeur=v
        self.suivante=s

class Pile:
    def __init__(self):
        self._contenu = None

    def est_vide(self):
        return self._contenu is None
    
    def empiler(self, e):
        self._contenu =  Cellule(e, self._contenu)

    def depiler(self):
        if self.est_vide():
            raise IndexError("Depile une pile vide")
        v=self._contenu.valeur
        self._contenu=self._contenu.suivante
        return v

    def consulter(self):
        if not self.estvide():
            return self._contenu.valeur

    def vider(self):
        self._contenu = None
            


def deplace(a, b, c, k):
    if k == 1 :
     temp=a.depiler()
     b.empiler(temp)
    else :
       deplace(a, c, b, k-1)
       deplace(a, b, c, 1)
       deplace(c, b, a, k-1)

def hanoi(n):
    p1=Pile()
    p2=Pile()
    p3=Pile()
    for i in range(1, n+1):
        p1.empiler(i)
    deplace(p1, p3, p2, n)

hanoi(3)