class Cellule:
    def __init__(self, v, s):
        self.valeur=v
        self.suivante=s

def longeur(lst):
    """version boucle"""
    n=0
    while lst is not None:
        n+=1
        lst=lst.suivante
    return n