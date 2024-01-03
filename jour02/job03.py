from job02 import Livre

class LivreBibliotheque(Livre):
    def __init__(self, title, author, pages):
        super().__init__(title, author, pages)
        self.__disponible = True

    def get_title(self):
        title = super().get_title()
        return title

    def get_author(self):
        author = super().get_author()
        return author

    def get_pages(self):
        pages = super().get_pages()
        return pages

    def set_title(self, string):
        super().set_title(string)

    def set_author(self, string):
        super().set_author(string)

    def set_pages(self, integer):
        super().set_pages(integer)

    def verification(self):
        return self.__disponible

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
