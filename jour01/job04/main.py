from personne import Personne

# On créer deux instances, et on leur donne les attributs nécessaires
torvalds_linus = Personne("Torvalds", "Linus")
stallman_richard = Personne("Stallman", "Richard")

# On imprime l'output des méthodes
presentation_linus = torvalds_linus.SePresenter()
presentation_richard = stallman_richard.SePresenter()

print(
    f"{presentation_linus}\n",
    f"{presentation_richard}"
)
