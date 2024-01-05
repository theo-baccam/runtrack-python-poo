class Forme:
    def aire(self):
        return 0


class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        if not (
            isinstance(longueur, (float, int))
            and isinstance(largeur, (float, int))
            and longueur > 0
            and largeur > 0
        ):
            raise ValueError("Les dimensions doivent êtres des nombres positifs")
        super().__init__()
        self.__longueur = longueur
        self.__largeur = largeur

    def aire(self):
        return self.__longueur * self.__largeur


def main():
    rectangle = Rectangle(6, 8)
    print(rectangle.aire())


if __name__ == "__main__":
    main()
