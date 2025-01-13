from file import *
from Main import *
from simulateur import *
from v2 import *

class FakeSimulateur:
    def __init__(self):
        self._totalAttente = 0
        self._tick = 0
        self.nbGuichets = 5

sim = Simulateur()

sim.config()

print(sim.guichets)
print(sim.max)
print(sim._repartiteur)
print(sim.nbTours)
print()
print(sim._tick)
print(sim._clientsServis)
print(sim._totalAttente)

