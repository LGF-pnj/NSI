from Pile import*

#fn parenthesee
def egeeEthra(ch, f):
    chpile=creer_pile()
    for i in range (len(ch)):
        if ch[i]=="(" or ch[i]==")":
            if chpile.est_vide():
                chpile.empiler(i)
            else :
                chpile.depiler()
                chpile.empiler(i)
        elif i == f:
            return chpile.depiler()
        
print(egeeEthra("(45+25)*((12+14)+4)", 15))
