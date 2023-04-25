class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def veillir(self):
        self.age += 1

animal=Animal()

print("Age initial de l'animal :", animal.age)

animal.veillir()
print("Age de l'animal après avoir veillit :", animal.age)
