class Produit:
    def __init__(self, input_name, input_price,  input_TVA):
        self.nom = input_name
        self.prixHT = input_price
        self.TVA = input_TVA

    def CalculerPrixTTC(self):
        TTC = self.prixHT + self.TVA
        return TTC

    def afficher(self):
        info_string = (
            f"Nom: {self.nom}\n"
            f"Prix hors-tarif: {self.prixHT}\n"
            f"TVA: {self.TVA}\n"
            f"TTC = {self.CalculerPrixTTC()}\n"
        )
        return info_string

    def changer_nom(self, new_name):
        self.nom = new_name

    def changer_prix(self, new_price):
        self.prixHT = new_price
