class Animal:
    # Init contient l'âge, et le nom, qui pour le moment est rien
    def __init__(self):
        self.age = 0
        self.prenom = None

    # Méthode pour augment l'âge
    def vieillir(self):
        self.age += 1
    
    # Méthode pour nommer l'animal
    def nommer(self, prenom):
        # Erreur si le prénom n'est pas un string
        if not isinstance(prenom, string):
            raise ValueError("Le prénom doit être un string")
        self.prenom = prenom
