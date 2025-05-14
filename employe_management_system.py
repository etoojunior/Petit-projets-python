from abc import ABC, abstractmethod

# Interface pour le calcul du salaire (équivalent en Python avec ABC)
class Salaire(ABC):
    @abstractmethod
    def calculer_salaire(self):
        pass

# Classe de base Employe
class Employe(Salaire):
    def __init__(self, nom, prenom, salaire_base, poste):
        self.__nom = nom
        self.__prenom = prenom
        self.__salaire_base = salaire_base
        self.__poste = poste

    # Propriétés (getters)
    @property
    def nom(self):
        return self.__nom

    @property
    def prenom(self):
        return self.__prenom

    @property
    def salaire_base(self):
        return self.__salaire_base

    @property
    def poste(self):
        return self.__poste

    # Setters
    @nom.setter
    def nom(self, valeur):
        self.__nom = valeur

    @prenom.setter
    def prenom(self, valeur):
        self.__prenom = valeur

    @salaire_base.setter
    def salaire_base(self, valeur):
        if valeur >= 0:
            self.__salaire_base = valeur

    @poste.setter
    def poste(self, valeur):
        self.__poste = valeur

    def calculer_salaire(self):
        return self.salaire_base

    def afficher_details(self):
        print(f"Employé: {self.prenom} {self.nom}")
        print(f"Poste: {self.poste}")
        print(f"Salaire: {self.calculer_salaire()}")

# Classe Manager qui hérite de Employe
class Manager(Employe):
    def __init__(self, nom, prenom, salaire_base, bonus, nombre_equipes):
        super().__init__(nom, prenom, salaire_base, "Manager")
        self.__bonus = bonus
        self.__nombre_equipes = nombre_equipes

    # Propriétés (getters)
    @property
    def bonus(self):
        return self.__bonus

    @property
    def nombre_equipes(self):
        return self.__nombre_equipes

    # Setters
    @bonus.setter
    def bonus(self, valeur):
        if valeur >= 0:
            self.__bonus = valeur

    @nombre_equipes.setter
    def nombre_equipes(self, valeur):
        if valeur >= 0:
            self.__nombre_equipes = valeur

    def calculer_salaire(self):
        return self.salaire_base + self.__bonus + (self.__nombre_equipes * 1000)

    def afficher_details(self):
        print(f"Manager: {self.prenom} {self.nom}")
        print(f"Poste: {self.poste}")
        print(f"Salaire: {self.calculer_salaire()}")
        print(f"Bonus: {self.__bonus}")
        print(f"Équipes gérées: {self.__nombre_equipes}")

# Classe Developpeur qui hérite de Employe
class Developpeur(Employe):
    def __init__(self, nom, prenom, salaire_base, specialite, heures_supplementaires):
        super().__init__(nom, prenom, salaire_base, "Developpeur")
        self.__specialite = specialite
        self.__heures_supplementaires = heures_supplementaires

    # Propriétés (getters)
    @property
    def specialite(self):
        return self.__specialite

    @property
    def heures_supplementaires(self):
        return self.__heures_supplementaires

    # Setters
    @specialite.setter
    def specialite(self, valeur):
        self.__specialite = valeur

    @heures_supplementaires.setter
    def heures_supplementaires(self, valeur):
        if valeur >= 0:
            self.__heures_supplementaires = valeur

    def calculer_salaire(self):
        return self.salaire_base + (self.__heures_supplementaires * 50)

    def afficher_details(self):
        print(f"Développeur: {self.prenom} {self.nom}")
        print(f"Poste: {self.poste}")
        print(f"Salaire: {self.calculer_salaire()}")
        print(f"Spécialité: {self.__specialite}")
        print(f"Heures supplémentaires: {self.__heures_supplementaires}")

# Test du système
if __name__ == "__main__":
    # Liste pour stocker tous les employés
    employes = []

    # Création de 2 employés
    employes.append(Employe("Leroy", "Paul", 3000, "Assistant administratif"))
    employes.append(Employe("Moreau", "Claire", 3200, "Comptable"))

    # Création de 3 managers
    employes.append(Manager("Dupont", "Jean", 5000, 1000, 3))
    employes.append(Manager("Lefevre", "Marie", 5200, 1200, 2))
    employes.append(Manager("Girard", "Luc", 5100, 1100, 4))

    # Création de 5 développeurs
    employes.append(Developpeur("Martin", "Sophie", 4000, "Python", 10))
    employes.append(Developpeur("Bernard", "Thomas", 4200, "Java", 8))
    employes.append(Developpeur("Robert", "Emma", 4100, "JavaScript", 12))
    employes.append(Developpeur("Petit", "Lucas", 4300, "C++", 15))
    employes.append(Developpeur("Roux", "Alice", 4050, "Php", 7))

    # Affichage des détails de tous les employés
    for i, employe in enumerate(employes, 1):
        print(f"\nEmployé {i}:")
        employe.afficher_details()
        print()