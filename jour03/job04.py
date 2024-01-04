class Joueur:
    def __init__(
        self, name, number, position, scored_goals, assists, yellow_cards, red_cards
    ):
        self.__name = name
        self.__number = number
        self.__position = position
        self.__scored_goals = scored_goals
        self.__assists = assists
        self.__yellow_cards = yellow_cards
        self.__red_cards = red_cards

    # Setters variés
    def marquerUnBut(self):
        self.__scored_goals += 1

    def effectuerUnePasseDecisive(self):
        self.__assists += 1

    def recevoirUnCartonJaune(self):
        self.__yellow_cards += 1

    def recevoirUnCartonRouge(self):
        self.__red_cards += 1

    # Ca permet d'obtenir les stats d'un joueur de façon structuré
    def afficherStatistiques(self):
        formatted_statistics = (
            f"Nom: {self.__name}\n"
            f"Numéro: {self.__number}\n"
            f"Position: {self.__position}\n"
            f"Buts marqués: {self.__scored_goals}\n"
            f"Passes décisives: {self.__assists}\n"
            f"Cartons jaunes reçus: {self.__yellow_cards}\n"
            f"Cartons rouges reçus: {self.__red_cards}\n"
            f"\n"
        )
        return formatted_statistics


class Equipe:
    def __init__(self, name):
        self.__name = name
        self.__player_list = []

    # On peut ajouter des joueurs dans une tuple pour éviter de rêpéter
    # la methode
    def ajouterJoueur(self, player):
        if isinstance(player, tuple):
            for individual in player:
                self.__player_list.append(individual)
            return
        self.__player_list.append(player)

    # Un string qui commence avec le nom de l'équipe, puis les stats des joueurs
    def AfficherStatistiquesJoueurs(self):
        team_statistics = f"--- {self.__name} ---\n"
        for player in self.__player_list:
            team_statistics += player.afficherStatistiques()
        return team_statistics

    # A part que ça aide à ne pas se tromper sur qui appartient à quelle équipe.
    # Cette méthode me paraît un peu redondante.
    def mettreAJourStatistiquesJoueur(self, player, method):
        if not player in self.__player_list:
            return
        method()


red = Equipe("RED")
# De ce que je comprends les nombres sont supposés être liés à la position
# Pas mon problème ¯\_(ツ)_/¯
demoman = Joueur("Tavish", 1, "Defense", 1, 4, 7, 3)
engineer = Joueur("Dell", 3, "Midfield", 9, 15, 3, 1)
soldier = Joueur("Jane", 4, "Forwards", 19, 12, 9, 27)
red.ajouterJoueur((demoman, engineer, soldier))

blu = Equipe("BLU")
heavy = Joueur("Misha", 7, "Defense", 3, 9, 3, 2)
pyro = Joueur("Mmmh Mmh-mhh!", 8, "Midfield", 8, 14, 8, 17)
scout = Joueur("Jeremy", 2, "Forwards", 17, 5, 6, 5)
blu.ajouterJoueur((heavy, pyro, scout))

print("--- DEBUT DE PARIE ---\n")
print(red.AfficherStatistiquesJoueurs())
print(blu.AfficherStatistiquesJoueurs())

blu.mettreAJourStatistiquesJoueur(pyro, pyro.effectuerUnePasseDecisive)
blu.mettreAJourStatistiquesJoueur(scout, scout.marquerUnBut)
blu.mettreAJourStatistiquesJoueur(scout, scout.recevoirUnCartonJaune)

blu.mettreAJourStatistiquesJoueur(heavy, heavy.effectuerUnePasseDecisive)
blu.mettreAJourStatistiquesJoueur(pyro, pyro.marquerUnBut)
blu.mettreAJourStatistiquesJoueur(scout, scout.recevoirUnCartonRouge)

red.mettreAJourStatistiquesJoueur(engineer, engineer.effectuerUnePasseDecisive)
red.mettreAJourStatistiquesJoueur(soldier, soldier.marquerUnBut)
red.mettreAJourStatistiquesJoueur(soldier, soldier.recevoirUnCartonJaune)

red.mettreAJourStatistiquesJoueur(demoman, demoman.effectuerUnePasseDecisive)
red.mettreAJourStatistiquesJoueur(engineer, engineer.marquerUnBut)

print("--- FIN DE PARTIE ---\n")
print(red.AfficherStatistiquesJoueurs())
print(blu.AfficherStatistiquesJoueurs())
