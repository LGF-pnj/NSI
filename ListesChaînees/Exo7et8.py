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

#correction en photo (?) sinon va voir sur ed
#aussi bon courage
#you got this



#exos 9 et 10 lol

#9
from ListeImport import Cellule

def listeN(n):
    if n==0:
        return None
    elif n==1:
        return 1
    else:
        return Cellule(listeN(n-1), n)


#10

def liste_tableau(t):
    lchai=None
    for i in range(0,len(t),-1):
        lchai=Cellule(t[i], lchai)
