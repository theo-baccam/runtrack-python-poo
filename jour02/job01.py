class Rectangle:
    # Nous initialisons des attributs privés longuers et largeurs
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # Afin de pouvoir intéragir avec les attributs privés, il faut utiliser des getters et setters.
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    def set_longueur(self, valeur):
        self.__longueur = valeur

    def set_largeur(self, valeur):
        self.__largeur = valeur


def main():
    # On crée un rectangle 10x5
    rectangle = Rectangle(10, 5)

    # On vérifie ses dimensions
    print(rectangle.get_longueur())
    print(rectangle.get_largeur())

    # On modifie ses dimensions
    rectangle.set_longueur(7)
    rectangle.set_largeur(19)

    # On re-vérifie ses dimensions
    print(rectangle.get_longueur())
    print(rectangle.get_largeur())


# On appel la fonction main que si on exécute directement le fichier
# Au cas où on souhaite exporter la classe.
if __name__ == "__main__":
    main()
