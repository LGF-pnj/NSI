from ListeImport import Cellule

def trouverec(x,lst):
    if lst is None :
        return 0
    elif lst.valeur == x :
        return trouverec(x, lst.suivante)
    else :
        return 1+trouverec(x, lst.suivante)
    
def trouvewh(x ,lst):
    i=0
    while lst.valeur != x:
        i+=1
        lst.suivante
