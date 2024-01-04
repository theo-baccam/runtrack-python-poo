from random import choice


class Personnage:
    def __init__(self, name, health_points):
        # verification du type des attributs
        if not isinstance(name, str):
            raise ValueError("Le nom du personnage doit être un string.")
        if not isinstance(health_points, int):
            raise ValueError("La vie d'un personnage doit être un integer")
        # Pour le moment, il n'y a que le strict minimum, mais je développerais tout ça plus tard.
        self.__name = name
        self.__health_points = health_points

    def get_name(self):
        return self.__name

    def get_health_points(self):
        return self.__health_points

    def lose_life(self, damage):
        self.__health_points -= damage

    def attaquer(self, target, damage):
        target.lose_life(damage)


class Jeu:
    # Toutes les méthodes s'initialise directement
    def __init__(self):
        self.__niveau = self.__choisirNiveau()
        self.__lancerJeu()

    # Prompt pour choisir et return le niveau
    def __choisirNiveau(self):
        while True:
            level_choice = input(
                f"Choisissez un niveau entre:\n"
                f"1) Facile\n"
                f"2) Intermédiaire\n"
                f"3) Difficile\n"
            )
            if level_choice == "1":
                return "Facile"
            elif level_choice == "2":
                return "Intermédiaire"
            elif level_choice == "3":
                return "Difficile"
            else:
                print("Choix invalide.\n")

    # Prompt pour le jeu lui même
    def __lancerJeu(self):
        if self.__niveau == "Facile":
            player_hp = 12
            enemy_hp = 8
        elif self.__niveau == "Intermédiaire":
            player_hp = 10
            enemy_hp = 10
        elif self.__niveau == "Difficile":
            player_hp = 8
            enemy_hp = 10
        # Initialisation personnages
        player = Personnage("Player", player_hp)
        enemy = Personnage("Enemy", enemy_hp)
        # Boucle du jeu
        while True:
            # print stats
            print(
                f"{player.get_name()}: {player.get_health_points()}HP\n"
                f"{enemy.get_name()}: {enemy.get_health_points()}HP"
            )
            # Choix aléatoire dommage
            player_choice = input()
            damage = choice(range(0, 3))
            player.attaquer(enemy, damage)
            # print dommage
            print(f"{player.get_name()} a attaqué pour {damage}HP")
            damage = choice(range(0, 3))
            enemy.attaquer(player, damage)
            print(f"{enemy.get_name()} a attaqué pour {damage}HP\n")
            # Resultat de la partie
            if player.get_health_points() <= 0:
                print("Le joueur est mort! L'ennemi gagne!")
                break
            elif enemy.get_health_points() <= 0:
                print("L'ennemi est mort! Le joueur gange")
                break


game = Jeu()
