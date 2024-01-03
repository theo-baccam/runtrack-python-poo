class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    def set_longueur(self, valeur):
        self.__longueur = valeur

    def set_largeur(self, valeur):
        self.__largeur = valeur

rectangle = Rectangle(10, 5)

print(rectangle.get_longueur())
print(rectangle.get_largeur())

rectangle.set_longueur(7)
rectangle.set_largeur(19)

print(rectangle.get_longueur())
print(rectangle.get_largeur())
