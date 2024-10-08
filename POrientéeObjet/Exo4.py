from math import pi, cos, sin

class Angle:
    def __init__(self,content):
        self.angle=content

    def __str__(self):
        return (str(self.angle)+" degrés")
    
    def ajoute(self, addm):
        self.angle = self.angle + addm.angle
        if self.angle > 360 :
            self.angle = self.angle % 360
    
    def cos(self):
        radSelf=self.angle*(pi/180)
        cos(radSelf)

    def sin(self):
        radSelf=self.angle*(pi/180)
        sin(radSelf)