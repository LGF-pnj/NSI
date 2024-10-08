class DbTab :
    def __init__(self, g, d):
        self.droite=d[:]
        self.gauche=[]
        for i in range(-1, -len(g)-1, -1):
            self.gauche.append(g[i])

def imin(self):
    mini=len(self.gauche)
    if mini!=0:
        mini=-mini
    return mini

def imax(self):
    return len(self.droite)-1

def append(self, elt):
    self.droite.append(elt)

def prepend(self, elt):
    self.gauche.append(elt)

def __getitem__(self, i):
    if i<0 :
        return self.gauche[-i-1]
    else :
        return self.droite[i]
    
def __setitem__(self, i, elt):
    if i<0 and i<len(self.gauche):
        self.gauche[i]=elt
    elif i>=0 and i>=len(self.droite)-1 :
        self.droite[i]=elt

def __str__(self):
    Btab=[]
    for elem in self.gauche[ : :-1]:
        Btab.append(elem)
    Btab.extend(self.droite)
    return Btab
