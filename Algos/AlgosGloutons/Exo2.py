from trav_data import *

def plus_proche(ville, dist, visitees):
    """renvoie un tableau contenant le numero de la ville non encore visitee la plus proche de la ville courant , 
    en supposant qu'il en exsiste au moins une et leur distance"""
    pp = None
    for i in range(len(visitees)):
        if visitees[i]:
            continue
        if pp == None or dist[ville][i]< dist[ville][pp] :
            pp = i
    return [pp, dist[ville][pp]]

def voyageur(villes, dist, depart):
    """Affiche les etapes du parcours glouton depuis la ville depart"""
    n = len(villes)
    visitees = [False] * n
    courante = depart
    tab_villes = []
    total_dist = 0
    for _ in range(n-1):
        visitees[courante] = True
        tab_villes.append(str(villes[courante]))
        s = plus_proche(courante, dist, visitees)
        suivante = s[0]
        total_dist += s[1]
        courante = suivante
    tab_villes.append(villes[depart])
    total_dist += dist[courante][depart]
    return [tab_villes, total_dist]

#answer :
print(voyageur(cities, plane_dist, ))
# et pr la dist elle est ici en centaines de miles, soit 527*100 = 52 700 miles

    