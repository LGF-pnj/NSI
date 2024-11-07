class Cellule:
    def __init__(self, v, s):
        self.valeur=v
        self.suivante=s

def longeur(lst):
    """version boucle"""
    n=0
    while lst is not None:
        n+=1
        lst=lst.suivante
    return n

def nieme_element(n,lst):
    """element indice n de la liste"""
    if lst is None :
        raise IndexError("indice invalide")
    elif n==0 :
        return lst.valeur
    else :
        return nieme_element(n-1, lst.suivante)

def concatener(l1,l2):
    if l1 is None :
        return l2
    else :
        return Cellule(l1.valeur, concatener(l1.suivante, l2))

def renverser(lst):
    r=None
    c=lst
    while c is not None:
        r=Cellule(c.valeur, r)
        c=c.suivante
    return r


# correction ex 1 q1
def str_liste(lst):
    if lst is None :
        return "\n"
    else :
        return str(lst.valeur) + "," + str_liste(lst.suivante)

class Liste:
    def __init__(self):
        self._tete = None
        
    def est_vide(self):
        return self._tete is None

    def ajoute(self, x):
        self._tete =Cellule(x, self._tete)

    def __len__(self):
        n=0
        c=self._tete
        while c is not None:
            n+=1
            c=c.suivante
        return n

    def __getitem__(self,n):
        return nieme_element(n, self._tete)

    def renverser(self):
        self._tete=renverser(self._tete)

    def __add__(self, lst):
        r=Liste()
        r._tete=concatener(self._tete, lst._tete)
        return r
    
    def __str__(self):
        return str_liste(self._tete)
