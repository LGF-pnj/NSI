
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
        #lorna
        # !!! bugged !!! i think.
        #self.repartiteurs[input()]
        #here
        #doesnt do what its supposed to
        """configure le simulateur selon les inputs des utilisateurs"""
        print("Mode de répartition ?")
        self._repartiteur=self.repartiteurs[input()]
        print("Nombre de guichets ?")
        self.nbGuichets=input()
        print("temps de traitement maximal aux guichets ?")
        self.max = input()
        print("nombres de tours de la simulation ?")
        self.nbTours = input()


    def demarre(self):
        """lance la simulation et retourne le nombre de clients servis et l'attente totale"""
        #boucle qui decremente tick(tt le tps)(actions entre)
        self._tick = 0
        #...
        return ("clients servis : "+str(self._clientsServis), "attente totale : "+str(self._totalAttente))