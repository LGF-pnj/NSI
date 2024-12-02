def parcours_infixe(a):
    """renvoie une chaine de caractères representant les elements de a en suivant un parcours infixe"""
    if a is None :
        return ""
    else :
        g=parcours_infixe(a.gauche)
        d=parcours_infixe(a.droit)
        return g + a.valeur + d

def remplir(a, t):
    if a is None :
        return t
    else :
        remplir(a.gauche, t)
        t.append(a.valeur)
        remplir(a.droite, t)



#lister dans abrimport