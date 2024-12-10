from ArborescencesImport import *
from Exo1 import affiche
from os import listdir, path

def repertoires(nom: str):
    Noeud(nom, )
    if path.isdir(nom):
        for elem in listdir(nom) :
            nom=path.join(nom, elem)
            return Noeud(elem, (repertoires(nom)))
        
print(listdir("/home/tnsi-eleve3/Documents/NSI/Arborescences/"))

affiche(repertoires("/home/tnsi-eleve3/Documents/NSI/Arborescences/"))    

#broken
#correction en photo

def repertoires2(nom: str):
    Noeud(nom, [])
    if path.isdir(nom):
        
        for elem in listdir(nom) :
            nom = a
            return Noeud(elem, [(repertoires2(nom))])
