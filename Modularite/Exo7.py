def tranche (t,i,j):
    newt=[]
    for elem in range(i,j):
        newt.append(t[elem])
    return newt

def concatenation (t1, t2):
    newt=list(t1)
    for elem in t2:
        newt.append(elem)
    return newt
