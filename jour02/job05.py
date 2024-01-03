class Voiture:
    def __init__(self, brand, model, year, mileage):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__mileage = mileage
        self.__reservoir = 50
        self.__en_marche = False

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_mileage(self):
        return self.__mileage

    def get_en_marche(self):
        return self.__en_marche

    def __verifier_plein(self):
        return self.__reservoir

    def set_brand(self, string):
        self.__brand = string

    def set_model(self, string):
        self.__model = string

    def set_year(self, integer):
        self.__year = integer

    def set_mileage(self, integer):
        self.__mileage = integer

    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True

    def arreter(self):
        self.__en_marche = False

def main():
    car = Voiture("Toyota", "Sprinter Trueno", 1983, 359)
    print(car.get_brand())
    print(car.get_model())
    print(car.get_year())
    print(car.get_mileage())
    print(car.get_en_marche())
    car.set_brand("Honda")
    car.set_model("Prelude")
    car.set_year(1998)
    car.set_mileage(219)
    car.demarrer()
    print(car.get_brand())
    print(car.get_model())
    print(car.get_year())
    print(car.get_mileage())
    print(car.get_en_marche())
    car.arreter()
    print(car.get_brand())
    print(car.get_model())
    print(car.get_year())
    print(car.get_mileage())
    print(car.get_en_marche())


if __name__ == "__main__":
    main()
