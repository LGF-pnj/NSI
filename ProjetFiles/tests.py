from file import *
from Main import *
from simulateur import *
from v2 import *


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