class Personne:
    def __init__(self,age=14):
        self.age = age

    def afficherAge(self):
        print("J'ai", self.age,"ans")

    def bonjour(self):
        print("Hello")
    
    def modifierAge(self,age):
        self.age = age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours.")

    def afficherAge(self):
        print("J'ai", self.age, "ans.")

class Professeur(Personne):
    def __init__(self,matiereEnseignee,age=30):
        super().__init__(age)
        self.__matiereEnseignee = matiereEnseignee

    def  enseigner(self):
        print("Le cours va commencer.")

eleve=Eleve()
print("L'élève a", eleve.age,"ans par défaut")
eleve.allerEnCours()
eleve.afficherAge()



