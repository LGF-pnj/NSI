from Exo1 import dist_Hamming

lexique = ["poussin", "vache", "lait", "main", "faille"]


def motdist(mot, dist, lex):
    for motL in lex :
        if dist_Hamming(mot, motL) == dist :
            print(motL)


