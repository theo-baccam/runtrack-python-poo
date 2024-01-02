class Personnage:
    # init contient position sur axe x et y
    def __init__(self, initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y

    # Méthodes pour déplacer le personnage
    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def bas(self):
        self.y -= 1

    def haut(self):
        self.y += 1

    # Méthode qui return la position
    def position(self):
        return (self.x, self.y)
