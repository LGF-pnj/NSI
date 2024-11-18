class Cellule:
    def __init__(self, v, s):
        self.valeur=v
        self.suivante=s

class Pile:
    def __init__(self):
        self._contenu = None

    def est_vide(self):
        return self._contenu is None
    
    def empiler(self, e):
        self._contenu =  Cellule(e, self._contenu)

    def depiler(self):
        if self.est_vide():
            raise IndexError("Depile une pile vide")
        v=self._contenu.valeur
        self._contenu=self._contenu.suivante
        return v


    def consulter(self):
        if not self.estvide():
            return self._contenu.valeur

    def vider(self):
        self._contenu = None

    def __len__(self):
        #copie ?? (correction : non tant)
        cmpt=0
        while self._contenu.suivante!=None:
            cmpt+=1
        self._contenu=self._contenu.suivante


def creer_pile():
    return Pile()


