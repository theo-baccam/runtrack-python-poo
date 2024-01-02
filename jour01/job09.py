class Produit:
    # init contient le nom, le prix hors tarif et le TVA
    def __init__(self, input_name, input_price, input_TVA):
        self.nom = input_name
        self.prixHT = input_price
        self.TVA = self.prixHT * (input_TVA / 100)

    # Méthode pour calculer le TTC
    def CalculerPrixTTC(self):
        TTC = self.prixHT + self.TVA
        return TTC

    # Méthode qui return les infos sur le produit
    def afficher(self):
        info_string = (
            f"Nom: {self.nom}\n"
            f"Prix hors-taxe: {self.prixHT}\n"
            f"TVA: {self.TVA}\n"
            f"TTC = {self.CalculerPrixTTC()}\n"
        )
        return info_string

    # Méthodes pour changer les attributs
    def changer_nom(self, new_name):
        self.nom = new_name

    def changer_prix(self, new_price):
        self.prixHT = new_price


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
