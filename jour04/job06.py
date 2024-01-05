class Vehicule:
    def __init__(self, brand, model, year, price):
        if not isinstance(brand, str):
            raise ValueError("La marque doit être un string")
        if not isinstance(model, str):
            raise ValueError("Le modèle doit être un string")
        if not isinstance(year, int):
            raise ValueError("L'annéee doit être un string")
        if not isinstance(price, (float, int)) or price < 0:
            raise ValueError("Le prix doit être un nombre positif")
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def informationsVehicule(self):
        print(
            f"Marque: {self.brand}\n"
            f"Modèle: {self.model}\n"
            f"Annéee: {self.year}\n"
            f"Prix: {self.price}\n"
        )


class Voiture(Vehicule):
    def __init__(self, brand, model, year, price):
        super().__init__(brand, model, year, price)
        self.portes = 4

    # Je comptais appeller la methode du parent et puis print les nombres de portes
    # Cependant beaucoup de problèmes concernant newline
    def informationsVehicule(self):
        print(
            f"Marque: {self.brand}\n"
            f"Modèle: {self.model}\n"
            f"Annéee: {self.year}\n"
            f"Prix: {self.price}\n"
            f"Nombre de portes: {self.portes}\n"
        )


class Moto(Vehicule):
    def __init__(self, brand, model, year, price, roue=2):
        super().__init__(brand, model, year, price)
        if not isinstance(roue, int) or roue <= 0:
            raise ValueError("Le nombre de roues doit ête un integer positif")
        self.roue = roue

    def informationsVehicule(self):
        print(
            f"Marque: {self.brand}\n"
            f"Modèle: {self.model}\n"
            f"Annéee: {self.year}\n"
            f"Prix: {self.price}\n"
            f"Nombre de roues: {self.roue}\n"
        )


def main():
    voiture = Voiture("Toyota", "Sprinter Trueno", 1998, 40000)
    voiture.informationsVehicule()

    moto = Moto("Marque", "Modèle", 2024, 19000)
    moto.informationsVehicule()


if __name__ == "__main__":
    main()
