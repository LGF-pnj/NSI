class Cellule:
    """une cellule d liste chainees"""
    def __init__(self,v,s):
        self._valeur=v
        self._suivante=s
        
    def __str__(self):
        #lorna
        if self is None :
            return ""
        if self._suivante is None :
            return str(self._valeur)
        else :
            return str(self._valeur) + ";" + str(self._suivante)

class File:
    """structure de file"""
    def __init__(self):
        self._tete=None
        self._queue=None
        self._longueur=0
    
    def est_vide(self):
        return self._tete is None
    
    def ajouter (self,e):
        c=Cellule(e, None)
        if self.est_vide():
            self._tete=c
        else:
            self._queue._suivante=c
        self._queue=c
        self._longueur+=1

    def retirer(self):
        if self.est_vide():
            raise IndexError("retire sur une file vide")
        v=self._tete._valeur
        self._tete=self._tete._suivante
        if self._tete is None:
            self._queue = None
        self._longueur-=1
        return v
        
    def __len__(self):
        return self._longueur
        
    def __str__(self):
        #lorna
        if self.est_vide():
            return ""
        else :
            return str(self._tete)