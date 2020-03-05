class CompteBancaire:
    """Ceci es la classe compte bancaire"""
    def __init__(self,NumeroCompte=0.0,NOM="",solde=0.0):
        """Initialisation d'un objet.

        Définition des attributs avec des valeurs par défaut.
        """
        self.NumeroCompte=NumeroCompte
        self.NOM=NOM
        self.solde=solde
    

    def Versement(self,prix):
        self.solde=(prix + self.solde)

    def Retrait(self, solde):
        return self.solde

    def Agio(self):
        return (self.solde * 5)/100

    def affichez(self):
        print(Nom)
        print(NumeroCompte)
        print(solde)



if __name__ == "__main__":
    # Insérez ici la suite de votre programme Python
    # qui va utiliser la classe CompteBancaire
    
    CB=CompteBancaire(115288789, "berenger", 500000)  
print(CB.NumeroCompte)
print(CB.NOM)
print(CB.solde)
CB.Versement(10000)
print(CB.solde)