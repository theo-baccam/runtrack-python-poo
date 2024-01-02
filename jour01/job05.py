class Point:
    # Les attributs init contiennent les positions x et y
    def __init__(self, x_input, y_input):
        self.x = x_input
        self.y = y_input

        # Erreur si les attributs ne sont pas des nombres
        if (
            not isinstance(self.x, int)
            and not isinstance(self.x, float)
            or not isinstance(self.y, int)
            and not isinstance(self.y, float)
        ):
            raise ValueError("Positions doit être integer ou float")

    # Méthode pour qui return la position sous forme de tuple
    def afficherLesPoints(self):
        coordinate = (self.x, self.y)
        return coordinate

    # Méthodes qui donnent les positions dans l'axe X et Y séparément
    def afficherX(self):
        return self.x

    def afficherY(self):
        return self.y

    # Méthodes qui permettent de changer x et y
    # Erreur si increment n'est pas nombre
    def changerX(self, increment):
        if not isinstance(increment, int) and not isinstance(increment, float):
            raise ValueError("Incrément doit être integer ou float")

        self.x += increment

    def changerY(self, increment):
        if not isinstance(increment, int) and not isinstance(increment, float):
            raise ValueError("Incréments doit être integer ou float")

        self.y += increment


# On créer un point et on lui donne une position
point_1 = Point(0, 0)

# On imprime les coordonnées
point_1_coordinate = point_1.afficherLesPoints()
print(point_1_coordinate)

# On imprime les positions sur les deux axes séparément
point_1_x = point_1.afficherX()
point_1_y = point_1.afficherY()
print(point_1_x, point_1_y)

# On change la position du point
point_1.changerX(1)
point_1.changerY(1)

# On imprime les nouvelles positions
point_1_x = point_1.afficherX()
point_1_y = point_1.afficherY()
print(point_1_x, point_1_y)
