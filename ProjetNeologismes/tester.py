alphab="abcdefghijklmnopqrstuvwxyz"

def creationdic():
  """crée et renvoie le dictionnaire de stockage des données"""
  Data = {}
  for lettre in alphab:
    Data[lettre]={}
    for lettre2 in alphab:
      Data[lettre][lettre2]=0
    Data[lettre]["fin"]=0
  return Data

def totalMot(mot,Data):
  """totalMotv0 ; totalv3"""
  length=(len(mot))
  for i in range(length-1):
    Data[mot[i]][mot[i+1]]+=1
  Data[mot[-1]]['fin']+=1
  return Data

data=creationdic()
e=totalMot('schtroumpf', data)
print(e)
pass