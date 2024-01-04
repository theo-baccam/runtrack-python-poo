class Livre:
    # Nous initialisons plusieurs attributs dans le constructeur et nous vérifions si ils corrects
    def __init__(self, title, author, pages):
        if not isinstance(title, str):
            raise ValueError("Titre doit être un string")
        if not isinstance(author, str):
            raise ValueError("Auteur doit être un string")
        if not isinstance(pages, int) or pages < 0:
            raise ValueError("Pages doit être un integer positif")
        self.__title = title
        self.__author = author
        self.__pages = pages

    # Des méthodes getters et setters
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_pages(self):
        return self.__pages

    # Nous vérifions que les valeurs utilisé pour les setters sont correct
    def set_title(self, string):
        if not isinstance(string, str):
            raise ValueError("Titre doit être un string")
        self.__title = string

    def set_author(self, string):
        if not isinstance(string, str):
            raise ValueError("Auteur doit être un string")
        self.__author = string

    def set_pages(self, integer):
        if not isinstance(integer, int) or integer < 0:
            raise ValueError("Pages doit être un integer positif")
        self.__pages = integer


def main():
    # Nous créeons un object book
    book = Livre("Dune", "Frank Herbert", 612)

    # On affiche les attributs de book
    print(f"{book.get_title()}\n" f"{book.get_author()}\n" f"{book.get_pages()}\n")

    # On modifie les attributs
    book.set_title("Kairo")
    book.set_author("Kiyoshi Kurosawa")
    book.set_pages(404)

    # On les affiche à nouveau
    print(f"{book.get_title()}\n" f"{book.get_author()}\n" f"{book.get_pages()}\n")


if __name__ == "__main__":
    main()
