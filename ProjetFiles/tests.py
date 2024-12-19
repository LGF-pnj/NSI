# si on a le temps : methode superconfig pr lancer plusieur simuatons et faire des stats
from file import *
from Main import *
from simulateur import *


class FakeSimulateur:
    def __init__(self):
        self._totalAttente = 0
        self._tick = 0

s1 = FakeSimulateur()
rep_alea = RepartiteurAlea(s1)




e=File()
print(len(e))
e.ajouter(4)
e.ajouter(3)
e.ajouter(6)
print(len(e))
e.retirer()
print(len(e))
e.ajouter(3)