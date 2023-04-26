import math

class Forme:
    def aire(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self, largeur,hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur
    
    def perimetre(self):
        return 2*(self.largeur + self.hauteur)
    def surface(self):
        return self.largeur * self.hauteur
    
class Cercle(Forme):
    def __init__(self,radius):
        self.radius = radius

    def aire (self):
        return math.pi * self.radius ** 2
    
rectangle = Rectangle(5,3)
print("Le périmètre du rectangle est", rectangle.perimetre())
print("La surface du reectangle est", rectangle.surface())
print("L'aire du rectangle est :", rectangle.aire())

cercle = Cercle(5)
print("L'aire du cercle est :", cercle.aire())