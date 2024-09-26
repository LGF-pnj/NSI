def cree():
    return [0]*6

def contient(s,x):
    iEntier = x//64
    bit= x%64
    return (s[iEntier] & (1 << bit) != 0)

def ajoute(s,x):
    iEntier=x//64
    bit= x%64
    s=[iEntier] = s[iEntier] | 1 << bit

def enumere(s):
    tab=[]
    for entier in s :
        for i in range(64):
            if entier & (i << 64)!=0 :
                tab+=i
    return tab

#shellig

def contient_doublon(t):
    """le tableau contient-il un doublon ?"""
    s=cree()
    for x in t:
        if contient(s,x) :
            return True
        ajoute(s,x)
    return False