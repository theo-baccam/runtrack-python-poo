class Voiture:
    def __init__(self, brand, model, year, distance):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__distance = distance
        self.__reservoir = 50
        self.__en_marche = False

    # Getters et setters pour les attributs
    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_distance(self):
        return self.__distance

    def get_en_marche(self):
        return self.__en_marche

    def __verifier_plein(self):
        return self.__reservoir

    # Les setters ont des conditions pour vérifier en cas d'erreur
    def set_brand(self, string):
        if not isinstance(string, str):
            raise ValueError("La marque doit être un string")
        self.__brand = string

    def set_model(self, string):
        if not isinstance(string, str):
            raise ValueError("Le modèle doit être un string")
        self.__model = string

    def set_year(self, integer):
        if not isinstance(integer, int):
            raise ValueError("L'année doit être un integer")
        self.__year = integer

    def set_distance(self, number):
        if isinstance(number, int) or isinstance(number, float) or number >= 0:
            self.__distance = number
        else:
            raise ValueError("Le kilométrage doit être un nombre positif")

    def set_reservoir(self, number):
        if isinstance(number, int) or isinstance(number, float) or number >= 0:
            self.__reservoir = number
        else:
            raise ValueError("La valeur de reservoir doit être un nombre positif")

    def demarrer(self):
        # le setter demarrage vérifie reservoir
        if self.__verifier_plein() > 5:
            self.__en_marche = True

    def arreter(self):
        self.__en_marche = False


def print_info(car):
    print(
        f"Marque: {car.get_brand()}\n"
        f"Modèle: {car.get_model()}\n"
        f"Année: {car.get_year()}\n"
        f"Kilométrage: {car.get_distance()}\n"
        f"En marche? {car.get_en_marche()}\n"
    )


def main():
    car = Voiture("Toyota", "Sprinter Trueno", 1983, 359)

    print("Infos initiales:")
    print_info(car)

    car.set_brand("Honda")
    car.set_model("Prelude")
    car.set_year(1998)
    car.set_distance(219)
    print("Infos modifiés:")
    print_info(car)

    print("Démarrage voiture:")
    car.demarrer()
    print_info(car)

    print("Arrêt voiture:")
    car.arreter()
    print_info(car)

    print("Tentative démarrage (pas assez dans réservoir):")
    car.set_reservoir(4)
    print_info(car)


if __name__ == "__main__":
    main()
