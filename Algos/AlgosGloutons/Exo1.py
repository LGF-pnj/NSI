villes = ["Nancy", "Metz", "Paris", "Reims", "Troyes"]

dist = [[0, 55, 303, 188, 183],
        [55, 0, 306, 176, 203],
        [303, 306, 0, 142, 153],
        [188, 176, 142, 0, 123],
        [183, 203, 153, 123, 0]]

def plus_proche(ville, dist, visitees):
    """renvoie e numero de la ville non encore visitee la plus proche de la ville courant , 
    en supposant qu'il en exsiste au moins une"""
    pp = None
    for i in range(len(visitees)):
        if visitees[i]:
            continue
        if pp == None or dist[ville][i]< dist[ville][pp] :
            pp = i
    return pp
    
def voyageur(villes, dist, depart):
    """Affiche les etapes du parcours glouton depuis la ville depart"""
    n = len(villes)
    visitees = [False] * n
    courante = depart
    for _ in range(n-1):
        visitees[courante] = True
        suivante = plus_proche(courante, dist, visitees)
        print("Trajet de ", villes[courante], " à ", villes[suivante], " en ", 
              dist[courante][suivante],"km")
        courante = suivante
    print("retour depuis ", villes[courante], " à la ville de depart ", villes[depart], " en ",
          dist[courante][depart], "km")


voyageur(villes, dist, 1)
#Metz - Nancy - Troyes - Reims - Paris - Metz(retour)