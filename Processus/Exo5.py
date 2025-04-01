import threading

ledA = threading.Lock()
ledB = threading.Lock()
ledC = threading.Lock()

def prog1():
    while True :
        ledA.acquire()
        print("led A : récupérée - 1")
        ledB.acquire()
        print("led B : récuperée - 2")
        ledA.release()
        ledB.release()

def prog2():
    while True :
        ledB.acquire()
        print("led B : récupérée - 1")
        ledC.acquire()
        print("led C : récuperée - 2")
        ledB.release()
        ledC.release()

def prog3():
    while True :
        ledC.acquire()
        print("led C : récupérée - 1")
        ledA.acquire()
        print("led A : récuperée - 2")
        ledC.release()
        ledB.release()

t1 = threading.Thread(target=prog1, args=[])
t2 = threading.Thread(target=prog2, args=[])
t3 = threading.Thread(target=prog3, args=[])
t1.start()
t2.start()
t3.start()


#Exo6
#Exclusion mutuelle : les tables
#Rétention en attente : transactions -> atomicité
#Non préemption :explicite.
#Attente circulaire : la première transaction attend S de a seconde et la seconde T de la première

