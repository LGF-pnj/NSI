from ImportArbres import *
from Exo4 import str_arbre



def parfait(h):
    if h==0:
        return None
    else :
        return Noeud(parfait(h-1), h, parfait(h-1))
    



print(str_arbre(parfait(12)))