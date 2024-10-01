class Chrono:
    """une classe pour représenter un temps mesuré en heures, 
    minutes et secondes """
    heure_max = 24
    def __init__(self, h, m, s):
        self._temps = 3600*h + 60*m + s
    
    def avance(self, s):
        self._temps += s

    def conversion(self):
        s = self._temps
        return (s // 3600, (s//60)%60, s%60)
    
    def __str__(self):
        h,m,s = self.conversion()
        return (str(h)+ "h" + str(m) + "m" + str(s) + "s")
    
t = Chrono(22,22,22)
t.avance(158)
print(t)