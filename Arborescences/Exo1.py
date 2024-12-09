from ArborescencesImport import *
ch="    "

def affiche(a, ch):
    print(a.valeur)
    for f in a.fils :
        print(ch)
        print(affiche(f, ch))
    
affiche(a, "    ")

#on peut mettre une valeur par defaut a ch ds. la def de fn --> def affiche(a, ch="")
#aussi on peut mettre une chaine vide dans ch et l'estoace on le rajoute dans print(affiche(f, ch+"  ")) pour pas avoir
#d'espace obligatoire en debut de toutes les valeurs. 
