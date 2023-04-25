class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def Sepresenter(self):
        return f"Je m'appelle {self.nom} {self.prenom}"
personne1 = Personne("Dupont","Jean")
print(personne1.Sepresenter())
personne2= Personne("Richard","Gamblin")
print(personne2.Sepresenter())
personne3= Personne("Xavier","Tuyau")
print(personne3.Sepresenter())