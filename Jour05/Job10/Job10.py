class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50
        
    def get_marque(self):
        return self.__marque
    
    def set_marque(self, marque):
        self.__marque = marque
        
    def get_modele(self):
        return self.__modele
    
    def set_modele(self, modele):
        self.__modele = modele
        
    def get_annee(self):
        return self.__annee
    
    def set_annee(self, annee):
        self.__annee = annee
        
    def get_kilometrage(self):
        return self.__kilometrage
    
    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage
        
    def get_en_marche(self):
        return self.__en_marche
    
    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche
        
    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
            print("La voiture démarre.")
        else:
            print("Le réservoir est presque vide, impossible de démarrer.")
    
    def arreter(self):
        self.__en_marche = False
        print("La voiture s'arrête.")
        
    def __verifier_plein(self):
        return self.__reservoir
        
# Instanciation d'une voiture
ma_voiture = Voiture("Renault", "Clio", 2015, 50000)

# Affichage des informations de la voiture
print("Marque :", ma_voiture.get_marque())
print("Modèle :", ma_voiture.get_modele())
print("Année :", ma_voiture.get_annee())
print("Kilométrage :", ma_voiture.get_kilometrage())
print("En marche :", ma_voiture.get_en_marche())

# Démarrage de la voiture
ma_voiture.demarrer()

# Arrêt de la voiture
ma_voiture.arreter()
