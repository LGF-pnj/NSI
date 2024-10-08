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