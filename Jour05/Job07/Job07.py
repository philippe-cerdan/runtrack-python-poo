class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True
    def get_titre(self):
        return self.__titre
    def set_titre(self,titre):
        self.__titre = titre
    def get_auteur(self):
        return self.__auteur
    def set_auteur(self, auteur):
        self.__auteur = auteur
    def get_nb_pages(self):
        return self.__nb_pages
    def set_nb_pages(self,nb_pages):
        self.__nb_pages = nb_pages
    def set_nb_pages(self, nb_pages):
        if isinstance(nb_pages, int) and nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            print("Le nombre de pages doit être un nombre entier positif.")
    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Le livre est déjà emprunté.")

    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre n'a pas été emprunté.")

#Création d'un livre
mon_livre = Livre("Le seigneur des anneaux","J.R.R. Tolkien", 1000)

print("Titre :", mon_livre.get_titre())
print("Auteur :", mon_livre.get_auteur())
print("Nombre de pages :", mon_livre.get_nb_pages())

mon_livre.set_titre("Le hobbit")
mon_livre.set_auteur("J.R.R. Tolkien")
mon_livre.set_nb_pages(500)

print("Titre :", mon_livre.get_titre())
print("Auteur :", mon_livre.get_auteur())
print("Nombre de pages :", mon_livre.get_nb_pages())

mon_livre.set_nb_pages(-100)

mon_livre.emprunter()
mon_livre.emprunter()
mon_livre.rendre()
mon_livre.rendre()