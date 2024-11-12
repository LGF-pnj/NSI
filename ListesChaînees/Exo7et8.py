from ListeImport import Cellule

def inserer(x,lst):
    if lst is None :
        return Cellule(x,None)
    elif x < lst.suivante.valeur :
        Cellule(x,lst.suivante)
        return 
    else :
        return inserer(x, lst.suivante)
    



def tri_par_insertion(lst):
    if lst is None :
        return None


















#"kepler!"