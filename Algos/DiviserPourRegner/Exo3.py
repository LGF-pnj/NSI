def fusion(t, g, m, d):
    n1 = m-g+1
    n2 = d-m
    lg=[]
    ld=[]
    for i in range(0, n1):
        lg[i]=t[g+i]
    for j in range(0, n2):
        ld[j]=t[m+1+j]
    lg[n1]=lg[n1-1]+1
    lg[n2]=lg[n2-1]+1
    i=0
    j=0
    for k in range(g, d+1):
        if lg[i]<=ld[j]:
            t[k]=lg[i]
            i=i+1
        else :
            t[k]=ld[j]
            j=j+1

def fusion2(t, g, m, d):
    n1 = m-g+1
    n2 = d-m
    lg=[]
    ld=[]
    for i in range(0, n1):
        lg[i]=t[g+i]
    for j in range(0, n2):
        ld[j]=t[m+1+j]
    i=0
    j=0
    for k in range(g, d+1):
        if lg[i]= or ld[j]=
        elif lg[i]<=ld[j]:
            t[k]=lg[i]
            i=i+1
        else :
            t[k]=ld[j]
            j=j+1