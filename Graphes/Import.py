class Grapheadj :
    """un graphe représenté par un dictionnaire d'adjacence"""
    def __init__(self):
        self.adj = {}

    def ajouter_sommet(self, s):
        if s not in self.adj :
            self.adj[s] = set()

    def ajouter_arc(self, s1, s2):
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        self.adj[s1].add(s2)

    def arc(self, s1, s2):
        return s2 in self.adj[s1]
    
    def sommets(self):
        return list(self.adj)
    
    def voisins(self, s):
        return self.adj[s]
    
    #exo8
    def nb_sommets(self):
        return len(self.adj)
    
    #exo10
    #q1
    #ne pend pas en charge les graphes non orientés
    def degré(self, s):
        return len(self.adj[s])
    
    #q2
    #ne pend pas en charge les graphes non orientés
    def nb_arcs(self):
        cmpt = 0
        for sommet in self.adj :
            cmpt += len(self.adj[sommet])
        return cmpt
    
    #q3
    #ne pend pas en charge les graphes non orientés
    def supprimer_arc(self, s1, s2):
        self.adj[s1].remove(s2)
    
    

class Graphemadj :
    """un graphe représenté par une matrice d'adjacence, où les sommets sont les entiers 0, 1, ..., n-1"""
    def __init__(self, n):
        self.n = n
        self.adj = [[False]*n for _ in range(n)]

    def ajouter_arc(self, s1, s2):
        self.adj[s1][s2] = True

    def arc(self, s1, s2):
        return self.adj[s1][s2]
    
    def voisins(self, s):
        v = []
        for i in range(self.n):
            if self.adj[s][i]:
                v.append[i]
        return v

    #exo9
    #q1
    #ne pend pas en charge les graphes non orientés
    def degré(self, s):
        return len(self.voisins(s))
    
    #q2
    #ne pend pas en charge les graphes non orientés
    def nb_arcs(self):
        cmpt = 0
        for i in range(len(self.adj)):
            for j in range(len(self.adj[i])):
                if self.adj[i][j]:
                    cmpt += 1
        return cmpt

    #q3
    #ne prend pas en charge les graphes non orientés
    def supprimer_arc(self, s1, s2):
        self.adj[s1][s2]=False


    