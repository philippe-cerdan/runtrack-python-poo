class Student:
    def __init__(self, nom, prenom, num_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiant = num_etudiant
        self.__nb_credits = 0
        self.__level = self.__studentEval()

    def __studentEval(self):
        if self.__nb_credits >= 90:
            return "Excellent"
        elif self.__nb_credits >= 80:
            return "Très bien"
        elif self.__nb_credits >= 70:
            return "Bien"
        elif self.__nb_credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def add_credits(self, credits):
        if credits > 0:
            self.__nb_credits += credits
            self.__level = self.__studentEval()

    def studentInfo(self):
        print("Nom : {}".format(self.__nom))
        print("Prénom : {}".format(self.__prenom))
        print("Identifiant : {}".format(self.__num_etudiant))
        print("Niveau : {}".format(self.__level))

# Instanciation d'un étudiant
john_doe = Student("Doe", "John", 145)

# Ajout de crédits
john_doe.add_credits(30)
john_doe.add_credits(35)
john_doe.add_credits(25)

# Affichage des informations de l'étudiant
john_doe.studentInfo()
