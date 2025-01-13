#config v1

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

#len de cellules       
def __len__(self):
    #lorna
    if self is None :
        return 0
    if self._suivante is None :
        return 1
    else :
        return 1+len(self._suivante)
    
#len de files (redirection)

def __len__(self):
    #lorna
    if self.est_vide():
        return 0
    else :
        return len(self._tete) 