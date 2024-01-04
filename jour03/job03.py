class Tache:
    def __init__(self, title, description):
        self.__title = title
        self.__description = description
        # Pour le status, j'utilise simplement un bool pour dire si c'est fini
        self.__done = False

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def get_done(self):
        return self.__done

    def set_done(self):
        self.__done = True


class ListeDeTaches:
    def __init__(self):
        # J'utilise un dictionnaire pour la liste de tâche car une tâche à
        # plusieurs attributs
        self.__task_list = {}

    # Methode permettant d'avoir une liste des tâches dans un format spécifique
    def afficherListe(self, filter_value=None):
        # Je vérifie si la liste est vide, sinon le programme va tenter
        # d'itérer dans une liste vide, ce qui pourrait causer une erreur
        if len(self.__task_list) == 0:
            return "Aucune tâche dans la liste pour le moment\n"

        formatted_list = ""

        # Il faut utiliser la méthode items afin d'avoir les keys et les valeurs
        for task, attributes in self.__task_list.items():
            title = task

            # j'attribut des variables aux slices  juste pour que ça soit
            # plus clair
            description = attributes[0]
            status = attributes[1]

            # Cette condition est là pour filtrer selon status
            if isinstance(filter_value, bool) and not status == filter_value:
                continue

            formatted_list += f"Titre: {title}\n" f"Description: {description}\n"

            # Condition pour décider quoi écrire en tant que status
            if status:
                formatted_list += f"Status: Terminé\n"
            else:
                formatted_list += f"Status: A faire\n"

            # ligne vide après liste pour méilleur visibilité
            formatted_list += "\n"
        return formatted_list

    # Si ce n'était pas requis, je l'aurais enlevé car c'est juste
    # afficherListe(bool)
    def filtrerListe(self, boolean):
        if not isinstance(boolean, bool):
            raise ValueError("Le paramètre doit être un boolean")
        return self.afficherListe(boolean)

    def ajouterTache(self, task):
        # Je donne le choix de mettre les tâches à modifier dans un tuple
        # afin d'éviter de rêpeter plusieurs fois la méthode
        if isinstance(task, tuple):
            for obj in task:
                # Je met les attributs dans une liste car c'est mutable.
                self.__task_list[obj.get_title()] = [
                    obj.get_description(),
                    obj.get_done(),
                ]
        else:
            self.__task_list[task.get_title()] = [
                task.get_description(),
                task.get_done(),
            ]

    def supprimerTache(self, task):
        if isinstance(task, tuple):
            for obj in task:
                self.__task_list.pop(obj.get_title())
        else:
            self.__task_list.pop(task.get_title())

    def marquerCommeFinie(self, task):
        if isinstance(task, tuple):
            for obj in task:
                self.__task_list[obj.get_title()][1] = True
            return
        self.__task_list[task.get_title()][1] = True


# On instancie une liste de tâches
task_list = ListeDeTaches()
print("--- LISTE SANS TACHES ---")
print(task_list.afficherListe())

# On instancie plusieurs tâches
brainstorm_composition = Tache("Compositions", "Brainstorm des compositions")
brainstorm_colors = Tache("Couleurs", "Brainstorm une palette de couleur à utiliser")
rough_sketch = Tache("Croquis", "Croquis basique")
linework = Tache("Linework", "Faire Linework")
coloring = Tache("Coloring", "Mettre les couleurs")
rendering = Tache("Shading", "Ombres")

task_list.ajouterTache(
    (
        brainstorm_composition,
        brainstorm_colors,
        rough_sketch,
        linework,
        coloring,
        rendering,
    )
)
print("--- LISTE AVEC TACHES ---")
print(task_list.afficherListe())

task_list.marquerCommeFinie(brainstorm_composition)
print("--- TACHE FINIE ---")
print(task_list.afficherListe())

task_list.supprimerTache((brainstorm_colors, coloring))
print("--- TACHES SUPPRIMEES ---")
print(task_list.afficherListe())

task_list.marquerCommeFinie((rough_sketch, linework))
print("--- TACHES FINIES ---")
print(task_list.afficherListe())

print("--- FILTRE TACHES FINIES ---")
print(task_list.filtrerListe(True))

print("--- FILTRES TACHES A FAIRE ---")
print(task_list.filtrerListe(False))
