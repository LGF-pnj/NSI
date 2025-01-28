def deplace(a, b, c, k):
    if k == 1 :
     print("déplace " +str(a)+" vers " +str(b))
    elif k == 2 :
       print("déplace " +str(a)+" vers " +str(c))
       print("déplace " +str(a)+" vers " +str(b))
       print("déplace " +str(c)+" vers " +str(b))
    else :
       deplace(a, b, c, k-1)
       print("déplace " +str(a)+" vers " +str(c))
       deplace(b, c, a, k-1)

deplace("1", "2", "3", 4)


