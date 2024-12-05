class Noeud :
    def __init__(self, v, f):
        self.valeur= v
        self.fils= f

def taille(a):
    t=1
    for f in a.fils:
        t += taille(f)
    return t

def parcours_prefixe(a):
    ch = a.valeur
    for f in a.fils:
        ch+= parcours_prefixe(f)
    return ch

a=Noeud("A", [Noeud("B", [Noeud("D", [])]), Noeud("C", [Noeud("E", []), Noeud("F", []), Noeud("G",[])])])