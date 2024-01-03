class Commande:
    def __init__(self, order_number, order_list):
        self.__order_number = order_number
        self.__order_list = order_list
        self.__order_status = "Ongoing"
        self.__total = self.__calculate_total()
        self.__TVA = 20 / 100
        self.__ttc = self.__calculate_ttc()


    def get_order_number(self):
        return self.__order_number

    def get_order_list(self):
        return self.__order_list

    def get_order_status(self):
        return self.__order_status

    def get_total(self):
        return self.__total

    def get_ttc(self):
        return self.__ttc

    def __calculate_ttc(self):
        tva = self.__total * self.__TVA
        ttc = self.__total + tva
        return ttc

    def __calculate_total(self):
        total = 0
        for value in self.__order_list.values():
            total += value
        return total

    def add_to_order(self, item, price):
        self.__order_list[item] = price
        self.__total = self.__calculate_total()
        self.__ttc = self.__calculate_ttc()

    def finish_order(self):
        self.__order_status = "Finished"

    def cancel_order(self):
        self.__order_status = "Cancelled"

def main():
    order_list = {
        "Large Peperonni Pizza": 9.20,
        "Medium Pineapple Pizza": 8.50,
        "3L Coke Bottle": 4.30,
    }
    order = Commande(492, order_list)
    print(
        f"Numéro: {order.get_order_number()}\n"
        f"Commandes: {order.get_order_list()}\n"
        f"Prix Hors-Taxe: {order.get_total()}\n"
        f"Prix TTC: {order.get_ttc()}\n"
        f"Status: {order.get_order_status()}\n"
    )

    order.add_to_order("Canette de Sprite", 1.40)
    print(
        f"Numéro: {order.get_order_number()}\n"
        f"Commandes: {order.get_order_list()}\n"
        f"Prix Hors-Taxe: {order.get_total()}\n"
        f"Prix TTC: {order.get_ttc()}\n"
        f"Status: {order.get_order_status()}\n"
    )


if __name__ == "__main__":
        main()

