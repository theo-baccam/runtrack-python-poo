from personnage import Personnage

# On instancie un nouveau personnage avec des coordonnées
john_doe = Personnage(0, 0)

# On affiche la position
position = john_doe.position()
print(position)

# Puis on la change, et on affiche la position modifié
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
