
from Pile import*

class Historique:
    def __init__(self):
        self.adresse_courante=None
        self._adresses_precedentes=creer_pile()
        self._adresses_suivantes=creer_pile()

    def aller_a(self, adr):
        if not self.adresse_courante is None:
            self._adresses_precedentes.empiler(self.adresse_courante)
        self.adresse_courante = adr
        self._adresses_suivantes=creer_pile()

    def retour(self):
        if not self._adresses_precedentes.est_vide():
            self._adresses_suivantes = self._adresses_suivantes.empiler(self.adresse_courante)
            self.adresse_courante = self._adresses_precedentes.depiler()
        else:
            self.adresse_courante = None

    def retour_avant(self):
        if not self._adresses_suivantes.est_vide():
            self.adresse_courante = self._adresses_suivantes.depiler()
        else :
            raise KeyError("pas d'adresses suivantes")


h=Historique()
assert h.adresse_courante is None
h.aller_a("www.stackoverflow.com")
assert h.adresse_courante == "www.stackoverflow.com"
h.aller_a("www.developer.com")
h.retour()
assert h.adresse_courante == "www.stackoverflow.com"
h.aller_a("www.w3schools.com")
h.aller_a("openclassroom.com")
h.retour
assert h.adresse_courante == "www.w3schools.com"
h.retour()
assert h.adresse_courante == "www.stackoverflow.com"

#
h.retour()
assert h.adresse_courante is None

#tests de retour avant
g=Historique
h.aller_a("www.stackoverflow.com")
h.retour()
h.retour_avant()
assert h.adresse_courante == "www.stackoverflow.com"
h.aller_a("openclassroom.com")
h.retour()
h.retour()
h.retour_avant()
assert h.adresse_courante == "www.stackoverflow.com"
h.aller_a("www.w3schools.com")
h.aller_a("www.developer.com")
h.retour()
