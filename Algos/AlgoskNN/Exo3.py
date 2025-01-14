from Exo2 import lexique
from Exo1 import dist_Hamming


def momin(motIN, lexique):
    dist = dist_Hamming(motIN, lexique[0])
    motMin = lexique[0]
    for i in range(len(lexique)) :
        if dist_Hamming(motIN, lexique[i])<dist:
            dist = dist_Hamming(motIN, lexique[i])
            motMin =  lexique[i]
    print(motMin)