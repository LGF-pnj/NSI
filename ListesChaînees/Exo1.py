from ListeImport import *
from FractonsImport import *
from random import randint

lst=Liste()
for i in range(6):
  num=randint(-10, 10)
  denom= randint(1,10)
  f=Fraction(num, denom)
  lst.ajoute(f)
#créee une liste chaînée de 6 fractions

print(lst)
