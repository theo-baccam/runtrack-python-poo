class Student:
    # les attributs de l'étudiant sont initialisé dans le constructeur
    def __init__(self, first_name, last_name, id_number):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__id_number = id_number
        self.__credit_number = 0
        self.__level = "Insuffisant"

    # Méthode pour attribuer un niveau à l'étudiant selon son crédit
    def __studentEval(self):
        if self.__credit_number >= 90:
            self.__level = "Excellent"
        elif self.__credit_number >= 80:
            self.__level = "Très bien"
        elif self.__credit_number >= 70:
            self.__level = "Bien"
        elif self.__credit_number >= 60:
            self.__level = "Passable"
        else:
            self.__level = "Insuffisant"

    # Méthode pour ajouter crédit
    def add_credits(self, integer):
        self.__credit_number += integer
        # Il faut re-attribuer un niveau à l'étudiant puisque le crédit à changé
        self.__studentEval()

    # Méthode qui retourne un string contenant les infos de l'étudiant
    def studentInfo(self):
        return (
            f"Nom: {self.__last_name}\n"
            f"Prénom: {self.__first_name}\n"
            f"Numéro étudiant: {self.__id_number}\n"
            f"Niveau: {self.__level}\n"
        )


def main():
    student = Student("John", "Doe", 145)
    print(student.studentInfo())

    student.add_credits(60)
    print(student.studentInfo())

    student.add_credits(10)
    print(student.studentInfo())

    student.add_credits(10)
    print(student.studentInfo())

    student.add_credits(10)
    print(student.studentInfo())


if __name__ == "__main__":
    main()
