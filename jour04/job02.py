# J'importe les classes à partir du fichier job01.py
from job01 import Personne, Eleve, Professeur


def main():
    eleve = Eleve()
    eleve.bonjour()
    eleve.allerEnCours()
    eleve.modifierAge(15)

    professeur = Professeur(40)
    professeur.enseigner()


if __name__ == "__main__":
    main()
