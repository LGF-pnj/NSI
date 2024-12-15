
class Simulateur:
    repartiteurs = {"Un" : "RepartiteurUn", "Alea" : "RepartiteurAlea", "Choix" : "RepartiteurChoix"}

    def __init__(self):
        self._repartiteur=None
        self._tick=None
        self._clientsServis=None
        self.max=None
        self.nbTours=None

    def config(self):
        """configure le simulateur selon les inputs des utilisateurs"""
        print("Mode de répartition ?")
        self._repartiteur=self.repartiteurs[input()]
        print("Nombre de guichets ?")
        #jsp attribut correspondant nn mentionne ds la description
        print("temps de traitement maximal aux guichets ?")
        self.max = input()
        print("nombres de tours de la simulation ?")
        self.nbTours = input()


    def demarre():
        pass
