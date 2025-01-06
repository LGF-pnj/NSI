<<<<<<< HEAD
=======
# si on a le temps : methode superconfig pr lancer plusieurs simulations et faire des stats
>>>>>>> fb1296f635ec7f24bab244b3046ec4821493b264
from file import *
from Main import *
from simulateur import *
from v2 import *

class FakeSimulateur:
    def __init__(self):
        self._totalAttente = 0
        self._tick = 0
        self.nbGuichets = 5

s2 = FakeSimulateur()
repAl = RepartiteurAlea(s2)


s3 = FakeSimulateur()
repCh = RepartiteurChoix(s3)

repCh.entree_client()
s3._tick+=1
repCh.entree_client()
s3._tick+=1
repCh.entree_client()
s3._tick+=1
repCh.entree_client()
s3._tick+=1
repCh.entree_client()
s3._tick+=1
repCh.entree_client()
s3._tick+=1
repCh.entree_client()
s3._tick+=1
repCh.entree_client()
s3._tick+=1
print(repCh.files[0])
print(repCh.files[1])
print(repCh.files[2])
print(repCh.files[3])
print(repCh.files[4])
