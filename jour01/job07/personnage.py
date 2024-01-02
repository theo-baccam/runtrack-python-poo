class Personnage:
    def __init__(self, initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def bas(self):
        self.y -= 1

    def haut(self):
        self.y += 1

    def position(self):
        return (self.x, self.y)
