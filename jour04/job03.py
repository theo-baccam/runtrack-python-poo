class Rectangle:
    def __init__(self, longueur, largeur):
        # Vérification attributs valide
        if not (
            isinstance(longueur, (float, int))
            and isinstance(largeur, (float, int))
            and longueur > 0
            and largeur > 0
        ):
            raise ValueError("Les dimensions doivent êtres des nombres positifs")
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    def set_longueur(self, number):
        if not isinstance(number, (float, int)) or number <= 0:
            raise ValueError("Les dimensions doivent êtres des nombres positifs")
        self.__longuer = number

    def set_largeur(self, number):
        if not isinstance(number, (float, int)) or number <= 0:
            raise ValueError("Les dimensions doivent êtres des nombres positifs")
        self.__longueur = number

    # J'ai songé à plutôt faire:
    # variable_a_retourner = (formule_mathematique)
    # return variable_a_retourner
    # Mais j'ai trouvé ça rédondant puisque la chose qu'on calcule est spécifié
    # dans le nom de la méthode.
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        if not isinstance(hauteur, (float, int)) or hauteur <= 0:
            raise ValueError("Les dimensions doivent êtres des nombres positifs")
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, number):
        if not isinstance(number, (float, int)) or number < 0:
            raise ValueError("Les dimensions doivent êtres des nombres positifs")

    def volume(self):
        return self.get_longueur() * self.get_hauteur() * self.__hauteur


def main():
    two_dimension = Rectangle(5, 10)
    print(
        f"--- RECTANGLE DIMENSIONS INITIALES ---\n"
        f"Longueur: {two_dimension.get_longueur()}\n"
        f"Largeur: {two_dimension.get_largeur()}\n"
        f"Perimètre: {two_dimension.perimetre()}\n"
        f"Surface: {two_dimension.surface()}\n"
    )

    two_dimension.set_longueur(7)
    two_dimension.set_largeur(8)
    print(
        f"--- RECTANGLE DIMENSIONS MODIFIEES ---\n"
        f"Longueur: {two_dimension.get_longueur()}\n"
        f"Largeur: {two_dimension.get_largeur()}\n"
        f"Perimètre: {two_dimension.perimetre()}\n"
        f"Surface: {two_dimension.surface()}\n"
    )

    three_dimension = Parallelepipede(8, 4, 12)
    print(
        f"--- PARALLELEPIPEDE DIMENSIONS INITIALES ---\n"
        f"Longueur: {three_dimension.get_longueur()}\n"
        f"Largeur: {three_dimension.get_largeur()}\n"
        f"Hauteur: {three_dimension.get_hauteur()}\n"
        f"Volume: {three_dimension.volume()}\n"
    )

    three_dimension.set_longueur(2)
    three_dimension.set_largeur(20)
    three_dimension.set_hauteur(15)
    print(
        f"--- PARALLELEPIPEDE DIMENSIONS MODIFIEES ---\n"
        f"Longueur: {three_dimension.get_longueur()}\n"
        f"Largeur: {three_dimension.get_largeur()}\n"
        f"Hauteur: {three_dimension.get_hauteur()}\n"
        f"Volume: {three_dimension.volume()}\n"
    )


if __name__ == "__main__":
    main()
