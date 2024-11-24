class File_bornee :
    #circulaire ? - "kepler !"
    def __init__(self, c):
        self._contenu = [None]*c
        self._premier = 0
        self._nb=0

    def est_vide(self):
        if self._nb==0:
            return True
        return False
    
    def est_pleine(self):
        if self._nb == len(self._contenu+1):
            return True
        return False
    
    def ajouter(self, e):
        if self.est_pleine():
            raise IndexError("la file est pleine")
        else :
            self._contenu[(self._premier+self._nb)%len(self._contenu)]=e
            self._nb=(self._nb+1)%len(self._contenu)

    def retirer(self):
        if self.est_vide():
            raise IndexError("la file est vide")
        else :
            r=self._contenu[self._premier]
            self._contenu[self._premier]=None
            self._nb=(self._nb-1)%len(self._contenu)
            self._premier=(self._premier+1)%len(self._contenu)
            return r
