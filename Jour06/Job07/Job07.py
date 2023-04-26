class Joueur:
    def __init__(self, argent=100):
        self.main = []
        self.argent = argent
        self.mise = 0

    def ajouter_carte(self, carte):
        self.main.append(carte)

    def vider_main(self):
        self.main = []

    def total_main(self):
        total = 0
        as_count = 0
        for carte in self.main:
            if carte.valeur in ["Valet", "Dame", "Roi"]:
                total += 10
            elif carte.valeur == "As":
                as_count += 1
            else:
                total += int(carte.valeur)
        total += as_count
        while total + 10 <= 21 and as_count > 0:
            total += 10
            as_count -= 1
        return total


class Partie:
    def __init__(self):
        self.jeu = Jeu()
        self.jeu.melanger()
        self.joueur = Joueur()
        self.croupier = Joueur()

    def jouer(self):
        while True:
            # Demander au joueur sa mise
            mise = int(input("Combien voulez-vous miser ? (votre argent : {})".format(self.joueur.argent)))
            if mise > self.joueur.argent:
                print("Vous n'avez pas assez d'argent.")
            else:
                self.joueur.argent -= mise
                self.joueur.mise = mise
                break

        # Distribuer les cartes initiales
        self.joueur.ajouter_carte(self.jeu.donner_carte())
        self.croupier.ajouter_carte(self.jeu.donner_carte())
        self.joueur.ajouter_carte(self.jeu.donner_carte())
        self.croupier.ajouter_carte(self.jeu.donner_carte())

        # Afficher la main du joueur et la première carte du croupier
        print("Main du joueur :")
        for carte in self.joueur.main:
            print(carte)
        print("Total : {}".format(self.joueur.total_main()))
        print("Première carte du croupier :")
        print(self.croupier.main[0])

        # Tour du joueur
        while True:
            choix = input("Voulez-vous prendre une carte (P) ou passer (S) ? ")
            if choix.upper() == "P":
                self.joueur.ajouter_carte(self.jeu.donner_carte())
                print("Nouvelle carte : {}".format(self.joueur.main[-1]))
                print("Total : {}".format(self.joueur.total_main()))
                if self.joueur.total_main() > 21:
                    print("Vous avez perdu !")
                    return
            elif choix.upper() == "S":
                break

        # Tour du croupier
        while self.croupier.total_main() < 17:
            self.croupier.ajouter_carte(self.jeu.donner_carte())

        # Afficher la main du croupier
        print("Main du croupier :")
        for carte in self.croupier.main:
            print(carte)
        print("Total : {}".format(self.croupier.total_main()))
# Déterminer le gagnant
        if self.joueur.total_main() > 21:
          print("Vous avez perdu !")
        elif self.croupier.total_main() > 21:
         print("Vous avez gagné !")
        elif self.joueur.total_main() > self.croupier.total_main():
         print("Vous avez gagné !")
        elif self.joueur.total_main() < self.croupier.total_main():
         print("Vous avez perdu !")
        else:
         print("Égalité !")

# Vider la main des joueurs pour la prochaine partie
        self.joueur.vider_main()
        self.croupier.vider_main()

    