import personne

torvalds_linus = personne.Personne("Torvalds", "Linus")
stallman_richard = personne.Personne("Stallman", "Richard")

presentation_linus = torvalds_linus.SePresenter()
presentation_richard = stallman_richard.SePresenter()

print(
    f"{presentation_linus}\n",
    f"{presentation_richard}"
)
