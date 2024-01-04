class CompteBancaire:
    def __init__(self, account_number, first_name, last_name, balance, decouvert):
        # Vérification type attributs
        if not isinstance(account_number, int):
            raise ValueError("Le numéro du compte doit être un integer")
        if not isinstance(first_name, str):
            raise ValueError("Le prénom doit être un string")
        if not isinstance(last_name, str):
            raise ValueError("Le nom doit être un string")
        if not isinstance(balance, (int, float)):
            raise ValueError("La solde doit être un nombre.")
        if not isinstance(decouvert, bool):
            raise ValueError("L'autorisation de découverte doit être un boolean.")
        self.__account_number = account_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__balance = balance
        self.__decouvert = decouvert
        self.__duree_decouvert = 90
        self.__interest_rate = 12 / 100

    # Ses getters permettent qu'un compte puissent obtenir
    # le nom et prénom d'un autre
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def afficher(self):
        affichage = (
            f"Numéro du compte: {self.__account_number}\n"
            f"Nom: {self.__last_name}\n"
            f"Prénom: {self.__first_name}\n"
        )
        # Afficher ceci selon autorisation découvert
        if self.__decouvert:
            affichage += f"Autorisation découverte: Oui\n"
        else:
            affichage += f"Autorisation découverte: Non\n"
        print(affichage)

    def afficherSolde(self):
        affichage = (
            f"{self.__last_name} {self.__first_name}:\nSolde: {self.__balance}€\n"
        )
        # Afficher agios si à découvert
        if self.__decouvert and self.__balance <= 0:
            affichage += f"Agios: {self.agios()}€\n"
        print(affichage)

    def agios(self):
        agios = (self.__decouvert * self.__duree_decouvert * self.__interest_rate) / 365
        return agios

    # setters
    def versement(self, value):
        self.__balance += value

    def retrait(self, value):
        if value > self.__balance and not self.__decouvert:
            print("Vous ne pouvez pas retirer plus que ce que vous possédez\n")
            return
        self.__balance -= value
        self.afficherSolde()

    def virement(self, reference, account, amount):
        self.retrait(amount)
        account.versement(amount)
        print(
            f"Référence: {reference}\n"
            f"De la part de: {self.__last_name} {self.__first_name}\n"
            f"Récipient: {account.get_last_name()} {account.get_first_name()}\n"
            f"Montant: {amount}€\n"
        )


def main():
    account_1 = CompteBancaire(1, "Bernard", "Ditry", 1000, False)
    account_1.afficher()
    account_1.afficherSolde()

    account_1.versement(500)
    account_1.retrait(700)
    account_1.retrait(850)

    account_2 = CompteBancaire(2, "Valentin", "Vaillou", 200, True)
    account_2.afficher()
    account_2.afficherSolde()

    account_2.retrait(300)

    account_1.virement("Sample Text", account_2, 250)
    account_2.afficherSolde()


if __name__ == "__main__":
    main()
