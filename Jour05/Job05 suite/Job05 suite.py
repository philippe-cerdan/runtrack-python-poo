class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
        

    def veillir(self):
        self.age += 1

    def name(self, prenom):
       self.prenom = prenom

animal = Animal()
print("Age initial de l'animal :", str(animal.age))

animal.veillir()
print("Age après veillissement :", str(animal.age))

animal.name("Uraken")
print(animal.prenom)

