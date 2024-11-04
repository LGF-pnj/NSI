#Exo1


#Exo2
def applique(f,t):
    newtab=[]
    for x in  t :
        newtab.append(f(x))
    return newtab

def applique_comp(f,t):
    newtab=[f(x) for x in t]
    return newtab

#Exo3

def calcule(op,f,t):
    v=f(t[0])
    for i in range(1, len(t)):
        v=op(v, f(t[i]))
    return v

#exemple

tab=[1,2,3,4]

def op(v,a):
    return v + ", " + a

def f(x):
    return str(x)

g=calcule(op, f, tab)

#Ex4
def compose(f,g):
    def h(x):
        return f(g(x))
    return h

#Ex5p1

def points(x,y):
    return (x,y)

a=points(2,-8)
b=points(4,17)
c=points(16,0)
d=points(-3,12)

def triangle(p1, p2, p3):
    return (p1,p2,p3)

def deplacer(p,dx,dy):
    return points(p[0]+dx, p[1]+dy)

def deplacer_triangle(t,dx,dy):
    return triangle(deplacer(t[0],dx,dy),deplacer(t[1],dx,dy),deplacer(t[2],dx,dy))

t1=triangle(a,b,c)
t2=triangle(b,c,d)

t3=deplacer_triangle(t1,-1,-1)
t4=deplacer_triangle(t2,2,3)

#ex5p2

#1. pas d'interêt ds. la config. actuelle -> potentiel selon modifs prévues.

ab=points(15,42)
bb=points(-28,384)
cb=points(-16,17)
db=points(0,1)

t1b=triangle(ab,bb,cb)
t2b=triangle(bb,cb,db)

t3b=deplacer_triangle(t1b,-1,-1)
t4b=deplacer_triangle(t2b,2,3)

print(t3b)
print(t4b)

#3,4 -> ? pas de pb ?