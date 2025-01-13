from Main import *

def mode_rep_valide(elem : str, self):
    if elem == "Un" : 
        return RepartiteurUn(self)
    if elem == "Aleatoire" : 
        return RepartiteurAlea(self)
    if elem == "Choix" : 
        return RepartiteurChoix(self)
    
def reesayez(attribut, validation, erreur : str, valAttribut=0) :
        while attribut == valAttribut :
            print(erreur)
            attribut = validation(input())
        return attribut

def reesayezRep(attribut, validation, erreur : str, self, valAttribut=0) :
        while attribut == valAttribut :
            print(erreur)
            attribut = validation(input(), self)
        return attribut

def int_valide(elem : str):
    if elem.isdigit() and int(elem)>0 :
        return int(elem)
    return 0


class Simulateur:
    repartiteurs = {"Un" : "RepartiteurUn", "Aleatoire" : "RepartiteurAlea", "Choix" : "RepartiteurChoix"}

    def __init__(self):
        self._repartiteur=None
        self._tick=None
        self._clientsServis=None
        self.max=None
        self.nbTours=None
        #attributs rajoutés
        self.nbGuichets=None
        self._totalAttente=None

    def config(self):
        """configure le simulateur selon les inputs des utilisateurs - v2"""
        print("Configuration du simulateur")
        print("nombres de tours de la simulation ?")
        self.nbTours = int_valide(input())
        #régler ca si on avait le temps : oral rip
        if self.nbTours == 0 :
            self.nbTours = reesayez(self.nbTours, int_valide, "Entrée invalide. Veuillez entrer un nombre strictement positif.")
        print("Nombre de guichets ?")
        nbGuichets = int_valide(input())
        if nbGuichets == 0 :
            nbGuichets = reesayez(nbGuichets, int_valide, "Entrée invalide. Veuillez entrer un nombre strictement positif.")
        for i in range(nbGuichets) :
            self.guichets.append(Guichet(self, i+1))
        print("temps de traitement maximal d'un client aux guichets, en nombre de tours ?")
        #vérif que input inf. nbtours ?
        self.max = int_valide(input())
        if self.max == 0 :
            self.max = reesayez(self.max, int_valide, "Entrée invalide. Veuillez entrer un nombre strictement positif.")
        if len(self.guichets) > 1 :
            print("Mode de répartition des clients ?")
            print(" - 'Un' : une file d'attente unique partagée par tous les clients")
            print(" - 'Aleatoire' : plusieurs files d'attentes, le client choisit aléatoirement entre elles ")
            print(" - 'Choix' : plusieurs files d'attentes, les clients choisissent la plus courte")
            self._repartiteur=mode_rep_valide(input(), self)
            if self._repartiteur == None :
                self._repartiteur = reesayezRep(self._repartiteur, mode_rep_valide, "Entrée invalide. Veuillez entrer une des possibilités proposées.", self, None)
        else :
            self._repartiteur=RepartiteurUn(self)

    def demarre(self):
        """lance la simulation et retourne le nombre de clients servis et l'attente totale"""
        #boucle qui decremente tick(tt le tps)(actions entre)
        self._tick = 0
        #...
        return ("clients servis : "+str(self._clientsServis), "attente totale : "+str(self._totalAttente))