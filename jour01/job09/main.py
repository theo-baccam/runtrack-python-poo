from produit import Produit

# On instancie deux objets
chips = Produit("Lays", 1.35, 20)
drink = Produit("Coca-Cola", 1.10, 20)

# On affiche les infos
chips_info = chips.afficher()
print(chips_info)

drink_info = drink.afficher()
print(drink_info)

# On change les infos et on re-affiche
chips.changer_nom("Pringles")
chips.changer_prix(1.60)
chips_info = chips.afficher()
print(chips_info)

drink.changer_nom("Sprite")
drink.changer_prix(1.20)
drink_info = drink.afficher()
print(drink_info)
