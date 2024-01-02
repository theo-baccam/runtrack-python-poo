class Personnage:
    # init contient position sur axe x et y
    def __init__(self, initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y

        # Erreur si les positions ne sont pas des integers
        # car ça doit correspondre à des index.
        if not isinstance(self.x, int) or not isinstance(self.y, int):
            raise ValueError("Positions doivent être des integers")

    # Méthodes pour déplacer le personnage
    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def bas(self):
        self.y -= 1

    def haut(self):
        self.y += 1

    # Méthode qui return la position
    def position(self):
        return (self.x, self.y)


# On instancie un nouveau personnage avec des coordonnées
john_doe = Personnage(0, 0)

# On affiche la position
position = john_doe.position()
print(position)

# Puis on la change, et on affiche la position modifié
john_doe.gauche()
position = john_doe.position()
print(position)

john_doe.droite()
position = john_doe.position()
print(position)

john_doe.bas()
position = john_doe.position()
print(position)

john_doe.haut()
position = john_doe.position()
print(position)
