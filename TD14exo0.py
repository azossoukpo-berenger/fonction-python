def cube(n):
    n=str(n)
    i=len(n)-1
    somme=0
    while (i>=0):
        somme+=pow(int(n[i]),3)
        i-=1
    if(somme==int(n)):
        return True
    else:
        return False
    
    

def recherche(nmaxi):
    for i in range(0,nmaxi+1):
        if cube(i) == True:
            print(i)

nmaxi=int(input("Entrer la borne supérieure "))
recherche(nmaxi)