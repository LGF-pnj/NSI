from file import *
from Main import *
from simulateur import *

#tick pas en param de entree client ds. les repartiteurs : pk ? justifier, discuter à l'oral

#documentation !

#(elucider la preference de repartiteurchoix)

#methode superconfig pr lancer plusieur simulations et faire des stats

# rajouter vérifs, prog.defensive + interface sympathique pour fn config
#client : pk creerclient ? si inutile replacer par appel simple Client(tick)
#variable ds.les files(class File) qui garde trace de la longueur pour eviter de len() 
#... systématiquement ds. repartiteurchoix



#rajouter les instances guichet ds. la liste des guichets + l'instance du bon repartiteur repartiteur dans l'attribut repartiteur

def configv2(self):
    print("Configuration du simulateur")
    print("nombres de tours de la simulation ?")
    #vérif que input intable + que entier pos.
    self.nbTours = int(input())
    print("Nombre de guichets ?")
    print("[Entier attendu. Exemple : 12]")
    #vérif que input intable + que entier pos.
    self.nbGuichets=int(input())
    print("temps de traitement maximal d'un client aux guichets, en nombre de tours ?")
    print("[Entier attendu. Exemple : 8]")
    #vérif que input intable + que entier pos. + que sup.0 et inf. nbtours
    self.max = int(input())
    if self.nbGuichets > 1 :
        print("Mode de répartition des clients ?")
        print(" - 'Un' : une file d'attente unique partagée par tous les clients")
        print(" - 'Aleatoire' : plusieurs files d'attentes, le client choisit aléatoirement entre elles ")
        print(" - 'Choix' : plusieurs files d'attentes, les clients choisissent la plus courte")
        #vérif que correspond bien à un des trois + modif. pr. avoir le bon appel (abandon de self.repartiteurs)
        self._repartiteur=self.repartiteurs[input()]
    else :
        self._repartiteur=RepartiteurUn(self)


def int_valide(elem):
    pass