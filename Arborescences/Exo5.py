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
        