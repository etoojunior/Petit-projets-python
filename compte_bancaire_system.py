from abc import ABC, abstractmethod

# Interface Transaction
class Transaction(ABC):
    @abstractmethod
    def depot(self, montant):
        pass

    @abstractmethod
    def retrait(self, montant):
        pass

# Classe de base CompteBancaire
class CompteBancaire(Transaction):
    def __init__(self, numero_compte, titulaire, solde_initial=0):
        self.__numero_compte = numero_compte
        self.__titulaire = titulaire
        self.__solde = solde_initial if solde_initial >= 0 else 0

    # Propriétés (getters)
    @property
    def numero_compte(self):
        return self.__numero_compte

    @property
    def titulaire(self):
        return self.__titulaire

    @property
    def solde(self):
        return self.__solde

    # Setter pour solde avec validation
    @solde.setter
    def solde(self, valeur):
        if valeur >= 0 or self._autorise_decouvert(valeur):
            self.__solde = valeur
        else:
            raise ValueError("Solde insuffisant ou découvert non autorisé.")

    # Méthode pour vérifier si le découvert est autorisé (à surcharger dans les sous-classes)
    def _autorise_decouvert(self, solde_propose):
        return False

    def depot(self, montant):
        if montant > 0:
            self.solde += montant
            print(f"Dépôt de {montant} effectué. Nouveau solde : {self.solde}")
        else:
            raise ValueError("Le montant du dépôt doit être positif.")

    def retrait(self, montant):
        if montant > 0:
            nouveau_solde = self.solde - montant
            if nouveau_solde >= 0 or self._autorise_decouvert(nouveau_solde):
                self.solde = nouveau_solde
                print(f"Retrait de {montant} effectué. Nouveau solde : {self.solde}")
            else:
                raise ValueError("Solde insuffisant pour le retrait.")
        else:
            raise ValueError("Le montant du retrait doit être positif.")

    def afficher_details(self):
        print(f"Compte {self.__numero_compte} - Titulaire : {self.__titulaire}")
        print(f"Solde : {self.__solde}")

# Classe CompteCourant
class CompteCourant(CompteBancaire):
    def __init__(self, numero_compte, titulaire, solde_initial=0, limite_decouvert=500):
        super().__init__(numero_compte, titulaire, solde_initial)
        self.__limite_decouvert = limite_decouvert if limite_decouvert >= 0 else 0

    @property
    def limite_decouvert(self):
        return self.__limite_decouvert

    @limite_decouvert.setter
    def limite_decouvert(self, valeur):
        if valeur >= 0:
            self.__limite_decouvert = valeur
        else:
            raise ValueError("La limite de découvert doit être positive ou nulle.")

    def _autorise_decouvert(self, solde_propose):
        return solde_propose >= -self.__limite_decouvert

    def afficher_details(self):
        super().afficher_details()
        print(f"Limite de découvert : {self.__limite_decouvert}")

# Classe CompteEpargne
class CompteEpargne(CompteBancaire):
    def __init__(self, numero_compte, titulaire, solde_initial=0, taux_interet=0.02):
        super().__init__(numero_compte, titulaire, solde_initial)
        self.__taux_interet = taux_interet if taux_interet >= 0 else 0

    @property
    def taux_interet(self):
        return self.__taux_interet

    @taux_interet.setter
    def taux_interet(self, valeur):
        if valeur >= 0:
            self.__taux_interet = valeur
        else:
            raise ValueError("Le taux d'intérêt doit être positif ou nul.")

    def appliquer_interet(self):
        interet = self.solde * self.__taux_interet
        self.solde += interet
        print(f"Intérêt de {interet} appliqué. Nouveau solde : {self.solde}")

    def afficher_details(self):
        super().afficher_details()
        print(f"Taux d'intérêt : {self.__taux_interet * 100}%")

# Programme principal pour tester le système
if __name__ == "__main__":
    # Création et test du compte courant
    print("=== Test du Compte Courant ===")
    compte_courant = CompteCourant("CC123", "Jean Dupont", 1000, 500)
    compte_courant.afficher_details()
    print("--- Opérations sur le compte courant ---")
    compte_courant.depot(500)
    compte_courant.retrait(1200)
    try:
        compte_courant.retrait(1000)  # Tentative de retrait dépassant le découvert
    except ValueError as e:
        print(f"Erreur : {e}")
    print("--- État final du compte courant ---")
    compte_courant.afficher_details()

    # Création et test du compte épargne
    print("\n=== Test du Compte Épargne ===")
    compte_epargne = CompteEpargne("CE456", "Marie Martin", 2000, 0.03)
    compte_epargne.afficher_details()
    print("--- Opérations sur le compte épargne ---")
    compte_epargne.depot(1000)
    compte_epargne.appliquer_interet()
    compte_epargne.retrait(500)
    try:
        compte_epargne.retrait(3000)  # Tentative de retrait dépassant le solde
    except ValueError as e:
        print(f"Erreur : {e}")
    print("--- État final du compte épargne ---")
    compte_epargne.afficher_details()