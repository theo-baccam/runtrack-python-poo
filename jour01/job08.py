# On importe la constante pi à partir du module math
from math import pi


class Cercle:
    # init ne contient que le rayon, on calcule le reste des attributs du cercle à partir du rayon
    def __init__(self, initial_rayon):
        self.rayon = initial_rayon

        # Si le rayon n'est pas un integer ou un float, erreur
        if not isinstance(self.rayon, int) and not isinstance(self.rayon, float):
            raise ValueError("Rayon doit être un integer ou un float")

    # Méthode pour changer le rayon
    def changerRayon(self, input_integer):
        self.rayon = input_integer

    # Méthode pour calculer les autres attributs
    def circonference(self):
        circonference = 2 * pi * self.rayon
        return circonference

    def aire(self):
        aire = pi * (self.rayon**2)
        return aire

    def diametre(self):
        diametre = self.rayon * 2
        return diametre

    # Méthode pour afficher les informations sur le cercle
    def afficherInfos(self):
        info_string = (
            f"Rayon = {self.rayon}\n"
            f"Diamètre = {self.diametre()}\n"
            f"Circonférence = {self.circonference()}\n"
            f"Aire = {self.aire()}\n"
        )
        print(info_string)


# On instancie deux cercles
cercle_1 = Cercle(4)
cercle_2 = Cercle(7)

# On affiche les informations sur ces deux cercles
cercle_1.afficherInfos()
cercle_2.afficherInfos()

# On modifie les rayons de ces cercles
cercle_1.changerRayon(13)
cercle_2.changerRayon(3)

# On re-affiche les infos
cercle_1.afficherInfos()
cercle_2.afficherInfos()
