from produit import Produit

chips = Produit("Lays", 1.35, 0.50)
drink = Produit("Coca-Cola", 1.10, 0.40)

chips_info = chips.afficher()
print(chips_info)

drink_info = drink.afficher()
print(drink_info)

chips.changer_nom("Pringles")
chips.changer_prix(1.60)
chips_info = chips.afficher()
print(chips_info)

drink.changer_nom("Sprite")
drink.changer_prix(1.20)
drink_info = drink.afficher()
print(drink_info)
