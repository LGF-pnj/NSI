import xml.dom.minidom as dom

docRecette=dom.parse("Arborescences/recette.xml")

def stat_xml(d):
    if dom.Node.ELEMENT_NODE == d.nodeType :
        e = 1
        a = 0
        t = 0

    elif dom.Node.TEXT_NODE == d.nodeType :
        e=0
        a=1
        t=0

    elif dom.Node.TEXT_NODE == d.nodeType :


import xml.dom.minidom as dom
import json
#exo6

def gen_doc(n):
    chChars="<a>"
    for i in range(n):
        chChars += " <b> " + str(i) + " </b>"
    chChars+=" </a>"
    doc = dom.parseString(chChars)
    #jsp comment sauver dans un fichier

#exo7

#hello_json.py :

with open("config.json", encoding ="utf8") as f:
    doc = json.load(f)

print doc[mode] + " " + doc[nom]
