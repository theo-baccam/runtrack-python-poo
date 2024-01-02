import personnage

john_doe = personnage.Personnage(0, 0)

position = john_doe.position()
print(position)

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
