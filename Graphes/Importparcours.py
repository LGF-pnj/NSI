from exercice_col import g

def parcours(g, vus, s):
    """parcours en profondeur depuis le sommet s"""
    if s not in vus :
        vus.add(s)
        for v in g.voisins(s) :
            parcours(g, vus, s)

def existe_chemin(g, u, v):
    """existe-t-il un chemin de u à v ?"""
    vus = set()
    parcours(g, vus, u)
    return v in vus


def parcours_largeur (g, source):
    """parcours en largeur depuis le sommet source"""
    dist = {source:0}
    courant = {source}
    suivant = set()
    while len(courant) > 0 :
        s = courant.pop()
        for v in g.voisins(s):
            if v not in dist :
                suivant.add(v)
                dist[v] = dist[s] + 1
        if len(courant) == 0 :
            courant, suivant = suivant, set()
    return dist

def distance(g, u, v):
    """distance de u à v et None si pas de chemin"""
    dist = parcours_largeur(g, u)
    return dist[v] if v in dist else None

#jeu de test :

assert distance(g, "Normandie", "Auvergne-Rhône-Alpes") == 2
assert distance(g, "Bretagne", "Bretagne") == 0
assert distance(g, "Grand Est", "Corse") == None

class Noeud :
    """un noeud d'un arbre binaire"""
    def __init__(self, g,v,d):
        self.gauche = g
        self.valeur = v
        self.droit = d
