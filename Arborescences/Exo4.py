import xml.dom.minidom as dom

docRecette=dom.parse("Arborescences/recette.xml")

def compte_balise(d, n):
    if d.nodeName==n:
        cmpt=1
    else :
        cmpt=0
    for child in d.childNodes :
        cmpt+=compte_balise(child, n)
    return cmpt
        
print(compte_balise(docRecette, "i"))

