class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print("J'ai", self.age, "ans")

    def bonjour(self):
        print("Hello")


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print("J'ai", self.age, "ans")


class Professeur(Personne):
    def __init__(self, age, matiereEnseignee):
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")

# Création d'un objet Eleve
eleve = Eleve(age=15)
eleve.bonjour()
eleve.allerEnCours()
eleve.affichageAge()

# Création d'un objet Professeur
professeur = Professeur(age=40, matiereEnseignee="Mathématiques")
professeur.bonjour()
professeur.enseigner()