from Pile import*

def calc_polonaise(ch):
    try :
        calc_curie(ch)
    except IndexError :
        return None
    except ValueError :
        return None

def calc_curie(ch):
    p=creer_pile()
    ctab=ch.split()
    for elem in ctab :
        if elem=="+":
            a=p.depiler()
            b=p.depiler()
            p.empiler(a+b)
        elif elem=="*":
            a=p.depiler()
            b=p.depiler()
            p.empiler(a*b)
        else:
            p.empiler(int(elem))
    result=p.depiler()
    if p.est_vide():
        return result
    else :
        return None


assert calc_curie("1 2 3 * + 4 *")==28
assert calc_curie("2 4 + 2 *")==12
assert calc_curie("0 19 * 2 +")==2
assert calc_curie("8")==8

assert calc_polonaise("8 7 2 4 +")==None
assert calc_polonaise("a b +")==None
assert calc_polonaise("8 4 6 7 2 15 468")==None
assert calc_polonaise("4 2 + 8 7 2")==None
assert calc_polonaise("* 0 2 + 7")==None
pass