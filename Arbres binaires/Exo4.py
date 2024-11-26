from ImportArbres import *

def str_arbre (a):
    if a is None :
        return ""
    else :
        return "(" + str_arbre(a.gauche) + str(a.valeur) + str_arbre(a.droit) + ")"
    
a = Noeud(Noeud(None, "B", Noeud(None, "C", None)), "A", Noeud(None, "D", None))
b = Noeud(Noeud(None, "B", Noeud(None, "C", None)), "A", Noeud(None, "D", None))
c= Noeud(None, "1", Noeud(None, "2", None))

print (str_arbre(a))
print(a==b)
print(a==c)