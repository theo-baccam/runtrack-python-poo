# Nous importons la classe Livre dans le fichier job02.py.
# Si nous n'avions pas mis la condition `if __name__ == "__main__"`,
# ça aurait exécuté le code qui est en dehors de la classe
from job02 import Livre


# Cette classe est l'enfant de la classe Livre
class LivreBibliotheque(Livre):
    def __init__(self, title, author, pages):
        # Cette classe hérite des attributs de son parent
        super().__init__(title, author, pages)
        # Un nouveau attribut pour la disponibilité
        self.__disponible = True

    # Cette class hérite aussi des méthodes de son parent,
    # donc pas besoin de les re-écrire.

    # verification est un getter qui retourne l'attribut disponible
    def verification(self):
        return self.__disponible

    # emprunter et rendre sont des setters qui modifie l'attribut disponible
    # on peut qu'emprunter si le livre a été rendu et vice-versa pour l'autre méthode
    def emprunter(self):
        if self.verification():
            self.__disponible = False

    def rendre(self):
        if not self.verification():
            self.__disponible = True


def main():
    book = LivreBibliotheque("Annihilation", "Jeff Vandermeer", 182)
    print(
        f"Info initiales:\n"
        f"{book.get_title()} par {book.get_author()}\n"
        f"{book.get_pages()} pages\n"
        f"Disponible: {book.verification()}\n"
    )

    book.set_title("Autorité")
    book.set_pages(263)
    print(
        f"Titre et pages changées:\n"
        f"{book.get_title()} par {book.get_author()}\n"
        f"{book.get_pages()} pages\n"
        f"Disponible: {book.verification()}\n"
    )

    book.emprunter()
    print(
        f"Livre emprunté:\n"
        f"{book.get_title()} par {book.get_author()}\n"
        f"{book.get_pages()} pages\n"
        f"Disponible: {book.verification()}\n"
    )

    book.rendre()
    print(
        f"Livre rendu:\n"
        f"{book.get_title()} par {book.get_author()}\n"
        f"{book.get_pages()} pages\n"
        f"Disponible: {book.verification()}\n"
    )


if __name__ == "__main__":
    main()
