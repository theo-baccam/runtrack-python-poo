class Point:
    # Les attributs init contiennent les positions x et y
    def __init__(self, x_input, y_input):
        self.x = x_input
        self.y = y_input

    # Méthode pour qui return la position sous forme de tuple
    def afficherLesPoints(self):
        coordinate = (self.x, self.y)
        return coordinate

    # Méthodes qui donnent les positions dans l'axe X et Y séparément
    def afficherX(self):
        return self.x

    def afficherY(self):
        return self.y

    # Méthodes qui permettent de changer x et y
    def changerX(self, increment):
        self.x += increment

    def changerY(self, increment):
        self.y += increment
