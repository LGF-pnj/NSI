from ABRImport import *
from random import randint

def trier(t):
    a=ABR()
    for elem in t :
        a.ajouter(elem)
    return a.lister()

print(trier([4, 2, 8, 6]))

# complexite :
# boucle for -->linéaire
# ajouter -->linéaire, Mais ds. boucle for --> quadratique
#remplir --> linéaire 



def melange(t):
    for i in range(len(t)):
        a=t[i]
        b=randint(0, i)
        t[i]=t[b]
        t[b]=a
    return t

#complexite :
#boucle for : linéaire.

def trierKnuth(t):
    a=ABR()
    g=melange(t)
    for elem in g :
        a.ajouter(elem)
    return a.lister()



