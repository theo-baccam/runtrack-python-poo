class Ville:
    def __init__(self, name, population):
        # On vérifie si les attributs sont du bon type
        if not isinstance(name, str):
            raise ValueError("Le nom de la ville doit être un string")
        if not isinstance(population, int):
            raise ValueError("La population doit être un integer")
        self.__name = name
        self.__population = population

    # Getters pour les attributs
    def get_name(self):
        return self.__name

    def get_population(self):
        return self.__population

    # Méthode pour ajouter à la population, utilisé par une Personne
    def ajouterPopulation(self):
        self.__population += 1


class Personne:
    def __init__(self, name, age, city):
        # Vérification type d'attribut
        if not isinstance(name, str):
            raise ValueError("Le prénom doit être un string")
        if not isinstance(age, int):
            raise ValueError("L'âge doit être un integer")
        if not isinstance(city, Ville):
            raise ValueError("La ville doit être une instance d'une classe")
        self.__name = name
        self.__age = age
        self.__city = city
        # On apelle la méthode ajouterPopulation de la Ville
        self.__city.ajouterPopulation()


def main():
    # On créer des instances de Ville
    paris = Ville("Paris", 1000000)
    marseille = Ville("Marseille", 861635)
    print(
        f"Population initiale:\n"
        f"{paris.get_name()}: {paris.get_population()}\n"
        f"{marseille.get_name()}: {marseille.get_population()}\n"
    )

    # On créer des instances de Personne, ce qui modifie la poulation de leur villes
    john = Personne("John", 45, paris)
    myrtille = Personne("Myrtille", 4, paris)
    chloe = Personne("Chloé", 18, marseille)
    print(
        f"Mis à jour population:\n"
        f"{paris.get_name()}: {paris.get_population()}\n"
        f"{marseille.get_name()}: {marseille.get_population()}\n"
    )


if __name__ == "__main__":
    main()
