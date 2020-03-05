class Rectangle:
    """Ceci est la classe Rectangle."""

    def __init__(self, long=0.0, larg=0.0):
        """Initialisation d'un objet.

        Définition des attributs avec des valeurs par défaut.
        """
        self.longueur = long
        self.largeur = larg


    def calcule_perimetre(self):
        """Méthode qui calcule le périmètre."""
        return ((self.longueur + self.largeur)/2)

    def calcule_surface(self):
        """Méthode qui calcule la surface."""
        return self.longueur * self.largeur
    def setlong(self,longueur):
        self.longueur=longueur
    def setlarg(self,largeur): 
        self.largeur=largeur
    def getlong(self):
        return self.longueur
    def getlarg(self):
        return self.largeur


class Parallelepipede(Rectangle):
    hauteur=0
    def __init__ (self,long=0.0,larg=0.0,hauteur=0.0):
        self.hauteur=hauteur
        Rectangle.__init__(self,long,larg)


    def calcule_volume(self):
        """Méthode qui calcule le volume."""
        return(self.longueur*self.largeur)*self.hauteur


if __name__ == "__main__":
    # Insérez ici la suite de votre programme Python
    # qui va utiliser la classe Rectangle.
    rectangle=Rectangle(10,15)
    pap=Parallelepipede(10,15,8)
    print(rectangle.longueur)
    print(rectangle.largeur)
    print(pap.hauteur)
    print(rectangle.calcule_perimetre())
    print(rectangle.calcule_surface())
    print(pap.calcule_volume ())
