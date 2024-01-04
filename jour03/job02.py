class CompteBancaire:
    def __init__(self, account_number, first_name, last_name, balance, decouvert):
        self.__account_number = account_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__balance = balance
        self.__decouvert = decouvert
        self.__duree_decouvert = 90
        self.__interest_rate = 12 / 100
        self.__agios = self.agios()

    def afficher(self):
        return self.__first_name, self.__last_name, self.__account_number

    def afficherSolde(self):
        return self.__balance

    def agios(self):
        if self.__balance >= 0:
            return 0
        agios = (self.__decouvert * self.__duree_decouvert * self.__interest_rate) / 365
        return agios

    def versement(self, value):
        self.__balance += value
        self.agios()

    def retrait(self, value):
        if value > self.__balance and not self.__decouvert:
            print("Vous ne pouvez pas retirer plus que ce que vous possédez")
            return
        self.__balance -= value
        self.__agios = self.agios()
        print(self.__balance)

    def virement(self, reference, account, amount):
        self.retrait(amount)
        account.versement(amount)
        print(f"{reference}\n{account.afficher()}\n{amount}")


account_1 = CompteBancaire(1, "Bernard", "Ditry", 1000, False)
print(account_1.afficher(), account_1.afficherSolde(), account_1.agios())

account_1.versement(500)
account_1.retrait(700)
account_1.retrait(850)

print(account_1.afficher(), account_1.afficherSolde(), account_1.agios())


account_2 = CompteBancaire(2, "Valentin", "Vaillou", 200, True)
print(account_2.afficher(), account_2.afficherSolde(), account_2.agios())
account_2.retrait(300)
account_1.virement("Sample Text", account_2, 250)
