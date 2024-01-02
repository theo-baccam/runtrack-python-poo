class Personne:
    # On met le nom et le prenom dans init
    def __init__(self, nom, prenom):
        self.personne_nom = nom
        self.personne_prenom = prenom

    # Méthode pour return une string qui présente la personne
    def SePresenter(self):
        presentation = f"Je suis {self.personne_prenom} {self.personne_nom}."
        return presentation
