class Calcule():
    def __init__(self):
        pass

    def factorielle(self, n):
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        return fact


    def somme(self,a,b):
        Somme=a+b
        return Somme

    def prem1(self,n) :
        for i in range (2,n) :
            if n%i == 0 : # n est divisible par i
                return False
                # On n’a pas trouvé de diviseur à l’entier n
        return True
    
    def tablmult(self,Z,Y):
        Produit= Z*Y
        return Produit

    def alltablesmult(self,N):
        for i in range(1,11):
            print(N,"X",i, "=",N*i)
        


if __name__ == "__main__":
    # Insérez ici la suite de votre programme Python
    # qui va utiliser la classe CompteBancaire
    calc=Calcule()
    print(calc.factorielle(5))
    print(calc.somme(5,8))
    print(calc.tablmult(6,2)) 
    print(calc.prem1(5))
    print(calc.alltablesmult(2))
        
        



    
 
