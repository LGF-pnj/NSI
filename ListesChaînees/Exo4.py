from ListeImport import Cellule

def trouverec(x,lst):
    if lst==None:
        return None
    if lst.valeur == x :
        return 0
    else :
            if trouverec(x, lst.suivante) !=None :
                return 1+trouverec(x, lst.suivante) 
            else :
                return None
        
    
def trouvewh(x ,lst):
    i=0
    while lst.valeur != x:
        i+=1
        lst=lst.suivante
    if i!=0:
        return i
    else :
        return None
