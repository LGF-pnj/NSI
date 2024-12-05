from ArborescencesImport import *
ch="    "

def affiche(a, ch):
    print(a.valeur)
    for f in a.fils :
        print(ch)
        print(affiche(f, ch))
    
affiche(a, "    ")
