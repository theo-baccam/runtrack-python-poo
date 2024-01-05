from math import pi

from job04 import Forme, Rectangle


class Cercle(Forme):
    def __init__(self, radius):
        if not isinstance(radius, (float, int)) or radius <= 0:
            raise ValueError("Le rayon doit être un nombre positif")
        super().__init__()
        self.__radius = radius

    def aire(self):
        return pi * (self.__radius**2)


def main():
    rectangle = Rectangle(3, 14)
    print(rectangle.aire())

    cercle = Cercle(5)
    print(cercle.aire())


if __name__ == "__main__":
    main()
