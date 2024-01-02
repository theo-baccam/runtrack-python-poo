class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = None

    def vieillir(self):
        self.age += 1

    def nommer(self, prenom):
        self.prenom = prenom
