class Commande:
    # On initialise le numéro de la commande et le dict contenant plâts et prix)
    def __init__(self, order_number, order_list):
        self.__order_number = order_number
        self.__order_list = order_list
        self.__order_status = "En cours"
        self.__prix_ht = self.__calculate_prix_ht()
        self.__TAUX_TVA = 20 / 100
        self.__tva = self.__calculate_tva()

    # Pour calculer la tva
    def __calculate_tva(self):
        tva = self.__prix_ht * self.__TAUX_TVA
        return tva

    # Pour calculer prix hors taxe
    def __calculate_prix_ht(self):
        prix_ht = 0
        for value in self.__order_list.values():
            prix_ht += value
        return prix_ht

    # Ajouter quelque chose à la commande
    def add_to_order(self, item, price):
        self.__order_list[item] = price
        # On recalcule le prix et la TVA
        self.__prix_ht = self.__calculate_prix_ht()
        self.__tva = self.__calculate_tva()

    def finish_order(self):
        self.__order_status = "Terminée"

    def cancel_order(self):
        self.__order_status = "Annulé"

    # Méthode pour obtenir la commande dans un format lisible
    def order_info(self):
        order_info = (
            f"Numéro: {self.__order_number}\n"
            f"Status: {self.__order_status}\n"
            f"----------------\n"
        )
        for item, price in self.__order_list.items():
            order_info += f"- {item}: {price}€\n"
        order_info += (
            f"----------------\n"
            f"Prix hors-taxe: {self.__prix_ht}€\n"
            f"TVA: {self.__tva}€\n"
            f"Total: {self.__prix_ht + self.__tva}€\n"
        )
        return order_info



def main():
    # Première commande
    first_order = {
        "Large Peperonni Pizza": 9.20,
    }
    first =  Commande(1, first_order)
    print(first.order_info())

    # Ajout
    first.add_to_order("3L Coke Bottle", 4.30)
    print(first.order_info())

    # Annulé
    first.cancel_order()
    print(first.order_info())

    # Deuxième commande
    second_order = {
        "Medium Pineapple Pizza": 8.50,
    }
    second = Commande(2, second_order)
    print(second.order_info())

    # Ajout
    second.add_to_order("Canette de Sprite", 1.40)
    print(second.order_info())

    # Terminé
    second.finish_order()
    print(second.order_info())


if __name__ == "__main__":
    main()
