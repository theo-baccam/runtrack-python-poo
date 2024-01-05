class Personne:
    def __init__(self, age=14):
        # Vérification argument
        if not isinstance(age, int) or age < 0:
            raise ValueError("L'âge doit être un integer positif")
        # Pas de raison que age soit un attribut privé
        self.age = age

    def afficherAge(self):
        print(self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, integer):
        if not isinstance(integer, int) or integer < 0:
            raise ValueError("L'âge doit être un integer positif")
        self.age = integer


class Eleve(Personne):
    def __init__(self, age=14):
        # super() permet d'hériter des méthodes et attributs du parent.
        super().__init__(age)

    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")


class Professeur(Personne):
    def __init__(self, age=23):
        super().__init__(age)

    def enseigner(self):
        print("Le cours va commencer")


def main():
    personne = Personne()

    eleve = Eleve()
    eleve.afficherAge()


if __name__ == "__main__":
    main()
