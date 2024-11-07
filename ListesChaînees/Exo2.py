from ListeImport import Cellule

def nieme_element(n,lst):
    """version av. boucle while"""
    if lst is None :
        raise IndexError("indice invalide")
    i=0
    while i !=n :
        lst=lst.suivante
        i+=1
    return lst.valeur




