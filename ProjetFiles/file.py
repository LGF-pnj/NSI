
class Cellule:
    """une cellule d liste chainees"""
    def __init__(self,v,s):
        self._valeur=v
        self._suivante=s
class File:
    """structure de file"""
    def __init__(self):
        self._tete=None
        self._queue=None
    
    def est_vide(self):
        return self._tete is None
    
    def ajouter (self,e):
        c=Cellule(e, None)
        if self.est_vide():
            self._tete=c
        else:
            self._queue.suivante=c
        self._queue=c

    def retirer(self):
        if self.est_vide():
            raise IndexError("retire sur une file vide")
        v=self._tete._valeur
        self._tete=self._tete._suivante
        if self._tete is None:
            self._queue = None
        return v
    
