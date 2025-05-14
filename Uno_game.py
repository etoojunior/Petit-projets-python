from abc import ABC, abstractmethod
import random

# Interface Jeu
class Jeu(ABC):
    @abstractmethod
    def distribuer(self, joueurs, nombre_cartes):
        pass

    @abstractmethod
    def jouer_tour(self):
        pass

# Classe de base Carte
class Carte:
    def __init__(self, couleur):
        self.__couleur = couleur

    @property
    def couleur(self):
        return self.__couleur

    @couleur.setter
    def couleur(self, valeur):
        if valeur in ["Rouge", "Bleu", "Vert", "Jaune", None]:
            self.__couleur = valeur

    def peut_etre_jouee(self, carte_actuelle):
        return False

    def effet(self, jeu):
        pass

    def __str__(self):
        return f"Carte {self.__couleur}"

# Classe pour les cartes normales (avec numéro)
class CarteNormale(Carte):
    def __init__(self, couleur, numero):
        super().__init__(couleur)
        self.__numero = numero

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, valeur):
        if 0 <= valeur <= 9:
            self.__numero = valeur

    def peut_etre_jouee(self, carte_actuelle):
        return (isinstance(carte_actuelle, Carte) and
                (self.couleur == carte_actuelle.couleur or
                 (isinstance(carte_actuelle, CarteNormale) and self.numero == carte_actuelle.numero)))

    def __str__(self):
        return f"Carte {self.couleur} {self.numero}"

# Classe pour les cartes +2
class CartePlusDeux(Carte):
    def __init__(self, couleur):
        super().__init__(couleur)

    def peut_etre_jouee(self, carte_actuelle):
        return (isinstance(carte_actuelle, Carte) and
                (self.couleur == carte_actuelle.couleur or
                 isinstance(carte_actuelle, CartePlusDeux)))

    def effet(self, jeu):
        # Le joueur suivant pioche 2 cartes et passe son tour
        jeu.piocher(jeu.joueurs[(jeu.tour_actuel + 1) % len(jeu.joueurs)], 2)
        jeu.tour_actuel += 1  # Passe le tour du joueur suivant
        print("Le joueur suivant pioche 2 cartes et passe son tour !")

    def __str__(self):
        return f"Carte Plus Deux ({self.couleur})"

# Classe pour les cartes Changement de couleur
class CarteChangerCouleur(Carte):
    def __init__(self):
        super().__init__(None)  # Pas de couleur initiale

    def peut_etre_jouee(self, carte_actuelle):
        return True  # Peut toujours être jouée

    def effet(self, jeu):
        if isinstance(jeu.joueurs[jeu.tour_actuel], Humain):
            # Pour le joueur humain, demander la couleur
            print("Choisissez une couleur : 1. Rouge, 2. Bleu, 3. Vert, 4. Jaune")
            while True:
                try:
                    choix = int(input("Entrez le numéro de la couleur : "))
                    if choix in [1, 2, 3, 4]:
                        nouvelle_couleur = ["Rouge", "Bleu", "Vert", "Jaune"][choix - 1]
                        self.couleur = nouvelle_couleur
                        print(f"Nouvelle couleur : {nouvelle_couleur}")
                        break
                    print("Choix invalide !")
                except ValueError:
                    print("Entrez un nombre valide !")
        else:
            # Pour l'ordinateur, choisir aléatoirement
            nouvelle_couleur = random.choice(["Rouge", "Bleu", "Vert", "Jaune"])
            self.couleur = nouvelle_couleur
            print(f"Nouvelle couleur choisie : {nouvelle_couleur}")

    def __str__(self):
        return f"Carte Changement de couleur ({self.couleur if self.couleur else 'Aucune'})"

# Classe JeuDeCartes
class JeuDeCartes(Jeu):
    def __init__(self):
        self.__pioche = []
        self.__defausse = []
        self.__couleurs = ["Rouge", "Bleu", "Vert", "Jaune"]
        self.__joueurs = []
        self.__tour_actuel = 0
        self.__initialiser_pioche()

    def __initialiser_pioche(self):
        # Cartes normales (0-9, deux de chaque sauf 0)
        for couleur in self.__couleurs:
            self.__pioche.append(CarteNormale(couleur, 0))
            for num in range(1, 10):
                self.__pioche.extend([CarteNormale(couleur, num)] * 2)
        # Cartes spéciales (+2, deux de chaque couleur)
        for couleur in self.__couleurs:
            self.__pioche.extend([CartePlusDeux(couleur)] * 2)
        # Cartes Changement de couleur (4 cartes)
        self.__pioche.extend([CarteChangerCouleur()] * 4)
        random.shuffle(self.__pioche)

    @property
    def pioche(self):
        return self.__pioche

    @property
    def defausse(self):
        return self.__defausse

    @property
    def joueurs(self):
        return self.__joueurs

    @property
    def tour_actuel(self):
        return self.__tour_actuel

    @tour_actuel.setter
    def tour_actuel(self, valeur):
        self.__tour_actuel = valeur

    def ajouter_joueur(self, joueur):
        self.__joueurs.append(joueur)

    def distribuer(self, joueurs, nombre_cartes=7):
        for joueur in joueurs:
            for _ in range(nombre_cartes):
                if self.__pioche:
                    joueur.ajouter_carte(self.__pioche.pop(0))

    def jouer_tour(self):
        pass  # Géré dans la boucle principale

    def piocher(self, joueur, nombre=1):
        for _ in range(nombre):
            if not self.__pioche:
                # Si la pioche est vide, remélanger la défausse
                self.__pioche = self.__defausse[:-1]  # Exclure la carte actuelle
                self.__defausse = [self.__defausse[-1]]  # Garder la carte actuelle
                random.shuffle(self.__pioche)
            if self.__pioche:
                joueur.ajouter_carte(self.__pioche.pop(0))

    def ajouter_defausse(self, carte):
        self.__defausse.append(carte)

    def carte_actuelle(self):
        return self.__defausse[-1] if self.__defausse else None

# Classe abstraite Joueur
class Joueur(ABC):
    def __init__(self, nom):
        self.__nom = nom
        self.__main = []

    @property
    def nom(self):
        return self.__nom

    @property
    def main(self):
        return self.__main

    def ajouter_carte(self, carte):
        self.__main.append(carte)

    def retirer_carte(self, index):
        return self.__main.pop(index) if 0 <= index < len(self.__main) else None

    @abstractmethod
    def jouer(self, jeu):
        pass

    def __str__(self):
        return f"{self.__nom} ({len(self.__main)} cartes)"

# Classe Humain
class Humain(Joueur):
    def jouer(self, jeu):
        print(f"\nTour de {self.nom}")
        print(f"Carte actuelle : {jeu.carte_actuelle()}")
        print("Votre main :")
        for i, carte in enumerate(self.main):
            print(f"{i}: {carte}")
        print(f"{len(self.main)}: Piocher")

        while True:
            try:
                choix = int(input("Choisissez une carte (index) ou piocher : "))
                if choix == len(self.main):
                    jeu.piocher(self)
                    print(f"{self.nom} a pioché une carte")
                    return None
                if 0 <= choix < len(self.main):
                    carte = self.main[choix]
                    if carte.peut_etre_jouee(jeu.carte_actuelle()):
                        jeu.ajouter_defausse(carte)
                        self.retirer_carte(choix)
                        carte.effet(jeu)
                        print(f"{self.nom} joue {carte}")
                        return carte
                    else:
                        print("Carte non jouable !")
                else:
                    print("Choix invalide !")
            except ValueError:
                print("Entrez un nombre valide !")

# Classe Ordinateur
class Ordinateur(Joueur):
    def jouer(self, jeu):
        print(f"\nTour de {self.nom}")
        print(f"Carte actuelle : {jeu.carte_actuelle()}")
        for i, carte in enumerate(self.main):
            if carte.peut_etre_jouee(jeu.carte_actuelle()):
                jeu.ajouter_defausse(carte)
                self.retirer_carte(i)
                carte.effet(jeu)
                print(f"{self.nom} joue {carte}")
                return carte
        jeu.piocher(self)
        print(f"{self.nom} a pioché une carte")
        return None

# Programme principal
if __name__ == "__main__":
    # Création des joueurs : 1 humain, 1 ordinateur
    joueurs = [
        Humain("Joueur"),
        Ordinateur("Ordinateur")
    ]

    # Initialisation du jeu
    jeu = JeuDeCartes()
    for joueur in joueurs:
        jeu.ajouter_joueur(joueur)

    # Distribution des cartes
    jeu.distribuer(joueurs)

    # Placer une carte initiale (éviter une carte spéciale au départ)
    while True:
        carte_initiale = jeu.pioche.pop(0)
        if isinstance(carte_initiale, CarteNormale):
            jeu.ajouter_defausse(carte_initiale)
            break
        jeu.pioche.append(carte_initiale)
        random.shuffle(jeu.pioche)

    # Boucle de jeu
    while all(len(joueur.main) > 0 for joueur in joueurs):
        joueur_actuel = joueurs[jeu.tour_actuel % len(joueurs)]
        carte_jouee = joueur_actuel.jouer(jeu)
        if len(joueur_actuel.main) == 0:
            print(f"\n{joueur_actuel.nom} gagne !")
            break
        if carte_jouee is None or not isinstance(carte_jouee, CartePlusDeux):
            jeu.tour_actuel += 1  # Passer au joueur suivant si pas +2