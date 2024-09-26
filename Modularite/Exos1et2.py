#modularité
#Exercice1

def cree():
    tab=[]
    return tab

def contient(s, x):
    if x in s :
        return True

def ajoute(s, x):
    s.append(x)


#Exercice2

def cree():
    s=0
    return s


#shellig

def contient_doublon(t):
    """le tableau contient-il un doublon ?"""
    s=cree()
    for x in t:
        if contient(s,x) :
            return True
        ajoute(s,x)
    return False

