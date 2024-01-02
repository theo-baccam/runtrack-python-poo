from animal import Animal

# On instancie un nouvel animal
chat = Animal()

# On affiche son âge
print(chat.age)

# On le fait vieillir
chat.vieillir()

# On re-affiche l'âge
print(chat.age)

# On nomme le chat
chat.nommer("Zia")

# On affiche le prénom
print(chat.prenom)
