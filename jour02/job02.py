class Livre:
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

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_pages(self):
        return self.__pages

    def set_title(self, string):
        self.__title = string

    def set_author(self, string):
        self.__author = string

    def set_pages(self, integer):
        self.__pages = integer

book = Livre("Dune", "Frank Herbert", 612)

print(
    f"{book.get_title()}\n"
    f"{book.get_author()}\n"
    f"{book.get_pages()}\n"
)

book.set_title("Kairo")
book.set_author("Kiyoshi Kurosawa")
book.set_pages(404)

print(
    f"{book.get_title()}\n"
    f"{book.get_author()}\n"
    f"{book.get_pages()}\n"
)
