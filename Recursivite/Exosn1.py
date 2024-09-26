#Exercice1
#1/--> tablette
#2/

def fact(n) :
    """renvoie l'entier n! pour tout entier positif"""
    if n==0 :
        return 1
    else : 
        return fact(n-1)*n
    
#Exercice2
#1/

def syracuse(un):
    while un>1 :
        if un%2 == 0 :
            var=syracuse(un-1)/2
            print (var)
            return var
        else :
            var=3*syracuse(un-1)+1
            print (var)
            return var
        

#Exercice3
#1/

def serie(n,a,b):
    if n==0:
        return ('a est un reel')
    elif n==1:
        return ('b est un reel')
    