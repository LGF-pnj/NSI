from ABRImport import Noeud

def ajoute(x, a):
    if a is None :
        return Noeud(None, x, None)
    elif x<a.valeur :
        return Noeud(ajoute(x,a.gauche), a.valeur, a.droit)
    elif x>a.valeur :
        return Noeud(a.gauche, a.valeur, ajoute(x, a.droit))
    else :
        return a