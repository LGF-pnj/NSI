alphab="abcdefghijklmnopqrsuvwxyz"

motsEn= { 
  "a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, 
  "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0,
  "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0
}


def load(fichier): #valide
  """ Fonction qui ouvre le fichier dictionnaire et renvoie le tableau des mots contenus"""
  with open(fichier, 'r') as f:
    fichier = [ligne.strip() for ligne in f.readlines()]
  return fichier


def MotDebutDic(fichierEn, motsEn): #valide sur données propres
  """renvoie le dictonnaire d'occurences de chaque lettre en début de mot à partir 
  du tableau des mots (par ordre alphabétique avec un séparateur) et du dictionnaire MotsEn"""
  i=-1
  motsEntotal = 0
  for ligne in fichierEn :
    if len(ligne) == 1 :
      i+=1
    else : 
     motsEn[alphab[i]]+=1
     motsEntotal+=1
  return(motsEn)

def total1(dic, Data):
  """v0"""
  t=[]
  for mot in dic :
    t.append(mot)
  return t

def total2(dic, Data):
  """v1"""
  for mot in dic:
    for i in range(len(mot)):
      if i==len(mot)-1:
        continue
      else :
       Data[mot[i]][mot[i+1]]+=1 
    Data[mot[-1]]["fin"] += 1
  return Data


def totalMot(mot,Data):
  """totalMotv0 ; totalv3"""
  length=(len(mot))
  for i in range(length-1):
    Data[mot[i]][mot[i+1]]+=1
  Data[mot[-1]]['fin']+=1
  return Data


def creationdic(): #valide
  """crée et renvoie le dictionnaire de stockage des données"""
  Data = {}
  for lettre in alphab:
    Data[lettre]={}
    for lettre2 in alphab:
      Data[lettre][lettre2]=0
    Data[lettre]["fin"]=0
  return Data

fichierEn= load("endic.txt")
fichierTest=load("testDic.txt")


