from ListeImport import Cellule

def occurencesrec(x, lst): 
    if lst is None:
        return 0
    elif lst.valeur == x :
        return 1+(occurencesrec(x, lst.suivante))
    elif lst.valeur != x:
        return occurencesrec(x, lst.suivante)
    

def occurenceswh(x,lst):
    occurences=0
    while lst!= None :
        if lst.valeur==x:
            ocurences+=1
        else :
            lst.suivante
    return occurences