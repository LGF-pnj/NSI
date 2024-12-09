from ArborescencesImport import *
ch="    "

def affiche(a, ch):
    print(a.valeur)
    for f in a.fils :
        print(ch)
        print(affiche(f, ch))
    
affiche(a, "    ")

#on peut mettre une valeir par defaut a ch ds. la def de fn --> def affiche(a, ch="")
#aussi on ne ceut pas un espace mais une chaîne vide.
