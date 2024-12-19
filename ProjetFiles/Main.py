from file import *
from random import randint
        
def _creerClient(tick):
    """cree un client à partir de l'horloge et le renvoie"""
    c=Client(tick)
    return c

class Repartiteur:
    #lorna
    def __init__(self,s):
        self.attenteTotale=0
        self.files=[]
        self.simul=s
    def entree_client(self):
        """ajoute un entier représentant le tour d'arrivée du client"""
        raise NotImplemented()
    
    def sortie_client(self,num):
        """retire un client de la file et ajoute son temps d'attente au total. 
        num est le numero du guichet."""
        raise NotImplemented()
    
class RepartiteurUn(Repartiteur):
    def __init__(self, s):
        super().__init__(s)
        f=File()
        self.files.append(f)

    def entree_client(self):
        c = _creerClient()
        self.files[0].ajouter(c)

    def sortie_client(self, num):
        c=self.files[0].retirer()
        self.simul._totalAttente += (self.simul._tick - c.temps_arrivee)


class RepartiteurAlea(Repartiteur):
    def __init__(self, s):
        super().__init__(s)
        for _ in range(self.simul.nbGuichets):
            f=File()
            self.files.append(f)
        
    def entree_client(self):
        c=_creerClient()
        ifile = randint(0, len(self.files)-1)
        self.files[ifile].ajouter(c)


    def sortie_client(self, num):
        #soit num le numero identifiant du guichet entre 1 et nbGuichets du simulateur inclus
        c = self.files[num-1].retirer()#-1 car passage de numero à indice ds le tableau files
        self.simul._totalAttente += (self.simul._tick - c.temps_arrivee)
        #on peut faire en sorte de renvoyer le client retiré ( pour le guichet.) Souhaitable ?
        

class RepartiteurChoix(Repartiteur):
    def __init__(self, s):
        super().__init__(s)
        for _ in range(self.simul.nbGuichets):
            f=File()
            self.files.append(f)

    def _lenfiles(self) -> list :
        lenfiles=[]
        for file in self.files :
            lenfiles.append[len(file)]
        return lenfiles

    def entree_client(self):
        c=_creerClient()
        ifile = min(self._lenfiles())
        self.files[ifile].ajouter(c)

    def sortie_client(self, num):
        pass
    
class Client:
    #lorna
    def __init__(self,tick):
        self.temps_arrivee=tick


class Guichet:
    #ludivine
    def __init__(self, s):
        self.simul = s
        self.traitement = None #jsp, a completer

    def tour(self):
        #appelle sortie client du repartiteur
        #fait : self.simul._clientsServis += 1 lorsqu'un client est traité (sort du guichet)
        pass


