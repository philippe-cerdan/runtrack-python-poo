class Vehicule:
    def __init__(self,marque,annee,prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix

    def informationVehicule(self):
        print("Marque :", self.marque)
        print("Année :", self.annee)
        print("Prix :", self.prix)

    def demarrer(self):
        print("Attention, je roule.")

class Voiture(Vehicule):
    def __init__(self, marque, annee, prix, portes=4):
        super().__init__(marque,annee,prix)
        self.portes = portes

    def informationVehicule(self):
        super().informationVehicule()
        print("Nombre de portes :", self.portes)
    
    def demarrer(self):
        print("Vroom vroom, je démarre !")

class Moto(Vehicule):
    def __init__(self, marque, annee, prix, roues=2):
        super().__init__(marque, annee, prix)
        self.roues = roues
    
    def informationVehicule(self):
        super().informationVehicule()
        print("Nombre de roues :", self.roues)

    def demarrer (self):
        print("En avant toute !")

ma_voiture = Voiture("Renault", 2022, 20000)
ma_voiture.informationVehicule()
ma_voiture.demarrer()


ma_moto = Moto("Yamaha", 2021, 8000)
ma_moto.informationVehicule()
ma_moto.demarrer()