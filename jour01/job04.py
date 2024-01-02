class Personne:
    # On met le nom et le prenom dans init
    def __init__(self, nom, prenom):
        self.personne_nom = nom
        self.personne_prenom = prenom

        # Si le nom ou le prénom n'est pas un string, mettre une erreur
        if not isinstance(nom, str) or not isinstance(prenom, str):
            raise ValueError("Nom ou Prénom doit être un string")

    # Méthode pour return un string qui présente la personne
    def SePresenter(self):
        presentation = f"Je suis {self.personne_prenom} {self.personne_nom}."
        return presentation


# On créer deux instances, et on leur donne les attributs nécessaires
torvalds_linus = Personne("Torvalds", "Linus")
stallman_richard = Personne("Stallman", "Richard")

# On imprime l'output des méthodes
presentation_linus = torvalds_linus.SePresenter()
presentation_richard = stallman_richard.SePresenter()

print(presentation_linus)
print(presentation_richard)
