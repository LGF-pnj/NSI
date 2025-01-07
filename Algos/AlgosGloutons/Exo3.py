euros = [1, 2, 5, 10, 20, 100, 200]

def monnaie(s):
    """nombre de pieces necessaires pour rendre la somme s"""
    i = len(euros)-1
    p = 0
    while s > 0 :
        if s >= euros[i]:
            s -= euros[i]
            p += 1
        else:
            i -= 1
    return p


print(monnaie(199))