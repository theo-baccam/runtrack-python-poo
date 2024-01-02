import point

point_1 = point.Point(0, 0)

point_1_coordinate = point_1.afficherLesPoints()

print(point_1_coordinate)

point_1_x = point_1.afficherX()
point_1_y = point_1.afficherY()

print(point_1_x, point_1_y)

point_1.changerX(1)
point_1.changerY(1)

point_1_x = point_1.afficherX()
point_1_y = point_1.afficherY()

print(point_1_x, point_1_y)
