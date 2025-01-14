def dist_Hamming(ch1, ch2):
    """renvoie la distance de Hamming (entier) entre deux chaînes de caractère passées en argument"""
    if ch1 is None :
        return len(ch2)
    if ch2 is None :
        return len(ch1)
    dist=0
    for i in range(min(len(ch1),len(ch2))):
        if ch1[i]!=ch2[i]:
            dist+=1
    dist+=abs(len(ch2)-len(ch1))
    return dist

