from math import pi

class Cercle:
    def __init__(self, initial_rayon):
        self.rayon = initial_rayon

    def changerRayon(self, input_integer):
        self.rayon = input_integer

    def circonference(self):
        circonference = 2 * pi * self.rayon
        return circonference

    def aire(self):
        aire = pi * (self.rayon ** 2)
        return aire

    def diametre(self):
        diametre = self.rayon * 2
        return diametre

    def afficherInfos(self):
        info_string = (
            f"Rayon = {self.rayon}\n"
            f"Diamètre = {self.diametre()}\n"
            f"Circonférence = {self.circonference()}\n"
            f"Aire = {self.aire()}\n"
        )
        print(info_string)
