class Personne:
    def __init__(self, nom, prenom):
        self.personne_nom = nom
        self.personne_prenom = prenom

    def SePresenter(self):
        presentation = f"Je suis {self.personne_prenom} {self.personne_nom}."
        return presentation
