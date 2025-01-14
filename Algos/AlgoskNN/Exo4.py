def obtainableminusone(c, d):
    if len(c)>=len(d):
        return False
    indD=0
    tolerance = True
    for i in range(len(c)):
        if c[i]!= d[indD] :
            if tolerance :
                tolerance = False
                indD+=1
            else :
                return False
        indD+=1
    return True
