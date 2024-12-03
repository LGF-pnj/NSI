from Exo5 import *

class Noeud :
    """un noeud d'un arbre binaire"""
    def __init__(self, g,v,d):
        self.gauche = g
        self.valeur = v
        self.droit = d

    def __eq__(self, subject):
        if self is None and subject is None :
            return True
        elif self.valeur == subject.valeur :
            return self.gauche==subject.gauche and self.droit==subject.droit
        else :
            return False 

def appartient(x, a):
    if a is None :
        return False
    elif x<a.valeur:
        return appartient(x, a.gauche)
    elif x>a.valeur :
        return appartient(x, a.droit)
    else : #egalite
        return True
    
def ajoute(x, a):
    if a is None :
        return Noeud(None, x, None)
    elif x<a.valeur :
        return Noeud(ajoute(x,a.gauche), a.valeur, a.droit)
    else :
        return Noeud(a.gauche, a.valeur, ajoute(x, a.droit))
    
def ajoute_enplace(x, a):
    assert a is not None
    if x<a.valeur :
        if a.gauche is None :
            a.gauche = Noeud(None, x, None)
        else :
            ajoute_enplace(x, a.gauche)
    else :
        if a.droit is None :
            a.droit = Noeud(None, x, None)
        else :
            ajoute_enplace(x, a.droit)

def supprime_minimum(a):
    assert a is not None 
    if a.gauche is None :
        return a.droit
    else :
        return Noeud(supprime_minimum(a.gauche), a.valeur, a.droit)


def str_arbre (a):
    if a is None :
        return ""
    else :
        return "(" + str_arbre(a.gauche) + str(a.valeur) + str_arbre(a.droit) + ")"
    
#Exo3
# 1.tout à droite

def minimum(a):
    if a is None :
        return None
    elif a.droite is None : 
        return a.valeur
    else :
        return minimum(a.droite)
    
def supprime(x, a):
    if a is None :
        return None
    elif x < a.valeur :
        return Noeud(supprime(x, a.gauche), a.valeur, a.droit)
    elif x > a.valeur :
        return Noeud(x, a.gauche, a.valeur, supprime(x, a.droit))
    elif a.droit is None:
        return a.gauche
    else :
        return Noeud(a.gauche, minimum(a.droit), supprime_minimum(a.droit))

class ABR :
    """un arbre binaire de recherche"""
    def __init__(self):
        self.racine= None

    def __contains__(self, x):
        return appartient(x, self.racine)
    
    def ajouter(self, x):
        self.racine=ajoute(x, self.racine)
        
    def taille(a):
        if a is None :
            return 0
        else : 
            return 1+ taille(a.gauche) + taille(a.droit)
            
    def hauteur(a):
        if a is None : 
            return 0
        else : 
            return 1+max(hauteur(a.gauche), hauteur(a.droit))

    def __str__(a):
        return str_arbre(a)
    
    def supp(self, x):
        return supprime(self.racine, x)
    
    def lister(self):
        t=[]
        return remplir(self, t)
    
    

        

