class Noeud :
    """un noeud d'un arbre binaire"""
    def __init__(self, g,v,d):
        self.gauche = g
        self.valeur = v
        self.droit = d

    def _eqeleve_(self, subject):
        if self is None and subject is None : #ligne imposssible car si self none on executera eq none et pas eq sur un noeud.
            return True
        elif self.valeur == subject.valeur :
            return self.gauche==subject.gauche and self.droit==subject.droit
        else :
            return False 

# non

    def __eq__(self, subject):
       return (subject is not None and self.valeur == subject.valeur and self.gauche==subject.gauche and self.droit == subject.droit)

def taille(a):
    """renvoie le nb de noeuds de l'arbre a"""
    if a is None:
        return 0
    else :
        return 1 + taille(a.gauche)+taille(a.droit)
    
def hauteur(a):
    """renvoie la hauteur de l'arbre a"""
    if a is None :
        return 0
    else :
        return 1 + max(hauteur(a.gauche), hauteur(a.droit))
    
def parcours_infixe(a):
    """renvoie une chaine de caractères representant les elements de a en suivant un parcours infixe"""
    if a is None :
        return ""
    else :
        g=parcours_infixe(a.gauche)
        d=parcours_infixe(a.droit)
        return g + str(a.valeur)+ d
