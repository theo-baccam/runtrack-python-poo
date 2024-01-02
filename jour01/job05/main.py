from point import Point

# On créer un point et on lui donne une position
point_1 = Point(0, 0)

# On imprime les coordonnées
point_1_coordinate = point_1.afficherLesPoints()
print(point_1_coordinate)

# On imprime les positions sur les deux axes séparément
point_1_x = point_1.afficherX()
point_1_y = point_1.afficherY()
print(point_1_x, point_1_y)

# On change la position du point
point_1.changerX(1)
point_1.changerY(1)

# On imprime les nouvelles positions
point_1_x = point_1.afficherX()
point_1_y = point_1.afficherY()
print(point_1_x, point_1_y)
