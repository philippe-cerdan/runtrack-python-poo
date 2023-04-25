class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur
    def set_longueur(self, longueur):
        self.__longueur = longueur
    def get_largeur(self):
        return self.__largeur
    def set_largeur(self, largeur):
        self.__largeur = largeur
mon_rectangle = Rectangle(10,5)      
print("La longueur de mon rectangle est :",mon_rectangle.get_longueur(), "et la largeur de mon rectangle est :", mon_rectangle.get_largeur()) 
mon_rectangle.set_longueur(20)
mon_rectangle.set_largeur(10)  
print("La nouvelle longueur de mon rectangle est :", mon_rectangle.get_longueur())
print("La nouvelle largeur de mon rectangle est :", mon_rectangle.get_largeur())