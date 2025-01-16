import os
import csv
from math import sqrt

def valide(ligne):
    ligne["petal_length"] = float(ligne["petal_length"])
    ligne["petal_width"] = float(ligne["petal_width"])
    ligne["species"] = int(ligne["species"])
    return ligne

def readCSV(rep, fic):
    fic = os.path.join(rep, fic)
    with open(fic, mode = "r", encoding="utf-8") as csvFile:
        reader = list(csv.DictReader(csvFile))
        lignes =[valide(ligne) for ligne in reader]
    return lignes

fleurs = readCSV("/home/tnsi-eleve3/Documents/NSI/Algos/AlgoskNN/TP/TP_classification_iris/", "iris.csv")

def distance(x1, y1, x2, y2):
    dist = sqrt(((x1-x2)**2)+((y1-y2)**2))
    return dist

def aj_distance(new_x, new_y, data):
    for ligne in data :
        ligne["distance"]=distance(ligne["petal_length"], ligne["petal_width"], new_x, new_y)

fakeflower=[{"petal_length":1.4, "petal_width": 0.2, "species":0},
            {"petal_length":1.8, "petal_width": 0.3, "species":2}]

def trier(data, cle):
    """tri_insertion, jsp"""
    for i in range(len(data)-1):
        key = data[i]
        j=i-1
        while j>=0 and data[j] > key :
            data[j+1]=data[j]
            j=j-1
        data[j+1]=key


