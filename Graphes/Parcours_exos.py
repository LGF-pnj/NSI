from Importparcours import parcours, Noeud
from exercice_col import g

#Ex5 :

def est_connexe(g):
    sommets = g.sommets()
    if sommets is None :
        return True
    source = sommets[0]
    vus = set()
    parcours(g, vus, source)
    for sommet in sommets :
        if not sommet in vus :
            return False
    return True

assert est_connexe(g) == False

#Ex6 :

def parcours_ch(g, vus, org, s):
    """parcours depuis le sommet s, en venant de org"""
    if s not in vus :
        vus[s] = org
        for v in g.voisins(s):
            parcours_ch(g, vus, )


def parcours(g, vus, s):
    """parcours en profondeur depuis le sommet s"""
    if s not in vus :
        vus.add(s)
        for v in g.voisins(s) :
            parcours(g, vus, s)


def chemin(g, u, v):
    """un chemin de u à v si il existe, None sinon"""
    pass

#ex7

a = Noeud(Noeud(None, "B", Noeud(None, "C", None)), "A", Noeud(None, "D", None))

def parcours_largeur(racine):
    dist = {racine.valeur : 0}
    courant = {racine}
    suivant = set()
    while len(courant)>0 :
        s = courant.pop()
        fils = set()
        if s.gauche != None :
            fils.add(s.gauche)
        if s.droit != None :
            fils.add(s.droit)
        for v in fils :
            if v.valeur not in dist :
                suivant.add(v)
                dist[v.valeur]= dist[s.valeur] + 1
        if len(courant) == 0 :
            courant, suivant = suivant, set()
    return dist

print(parcours_largeur(a))
