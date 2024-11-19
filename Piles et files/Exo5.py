from Pile import*

def verif_parentheses(ch):
    p1=creer_pile()
    p2=creer_pile()
    for char in ch :
        if char == "(":
            p1.empiler(char)
        elif char == "[":
            p2.empiler(char)
        elif char == ")" and not p1.est_vide():
            p1.depiler()
        elif char == "]" and not p2.est_vide():
            p2.depiler()
        elif char==")" or char=="]":
            return False
    if p1.est_vide() and p2.est_vide():
        return True
    return False
        

#tests

assert verif_parentheses("(2+5)*[9*6+(2-3)]")

assert verif_parentheses("(2+5 -[2*5]+4")==False


