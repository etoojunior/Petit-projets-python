import random
import json
import os

FICHIER_SCORES = "resultats_pierre_papier_ciseaux.json"

def charger_donnees():
    if os.path.exists(FICHIER_SCORES):
        with open(FICHIER_SCORES, "r") as f:
            return json.load(f)
    return {}

def sauvegarder_donnees(donnees):
    with open(FICHIER_SCORES, "w") as f:
        json.dump(donnees, f, indent=4)

def afficher_score(scores):
    print("\n📊 Score actuel :")
    print(f"✅ Victoires : {scores['victoires']}")
    print(f"❌ Défaites : {scores['defaites']}")
    print(f"🟡 Égalités : {scores['egalites']}")

def determiner_gagnant_global(nom_joueur, scores):
    victoires_joueur = scores['victoires']
    victoires_ordinateur = scores['defaites']  # Les défaites du joueur sont les victoires de l'ordinateur
    print(f"\n🏆 Résultat final après 5 tours :")
    if victoires_joueur > victoires_ordinateur:
        print(f"Félicitations {nom_joueur} ! Vous avez gagné contre l'ordinateur avec {victoires_joueur} victoires contre {victoires_ordinateur} !")
    elif victoires_ordinateur > victoires_joueur:
        print(f"L'ordinateur a gagné avec {victoires_ordinateur} victoires contre {victoires_joueur} pour {nom_joueur}.")
    else:
        print(f"Égalité ! {nom_joueur} et l'ordinateur ont chacun {victoires_joueur} victoires.")

def jouer_pierre_papier_ciseaux():
    choix_possibles = ["pierre", "papier", "ciseaux"]
    donnees = charger_donnees()
    total_tours = 5
    
    # Demander le nom du joueur
    nom_joueur = input("🧑 Entrez votre nom : ").strip()
    if not nom_joueur:
        print("⛔ Le nom ne peut pas être vide.")
        return
    
    # Initialiser les données du joueur s'il n'existe pas
    if nom_joueur not in donnees:
        donnees[nom_joueur] = {
            "scores": {"victoires": 0, "defaites": 0, "egalites": 0},
            "parties": []
        }
    
    donnees_joueur = donnees[nom_joueur]
    
    print(f"\n=== 🎮 Jeu de Pierre-Papier-Ciseaux pour {nom_joueur} ===")
    print("Choisissez : pierre, papier ou ciseaux")
    print(f"Vous jouerez {total_tours} tours.")
    
    tours_restants = total_tours
    while tours_restants > 0:
        print(f"\nTour {total_tours - tours_restants + 1}/{total_tours}")
        # Choix du joueur
        joueur = input("Votre choix : ").lower().strip()
        
        if joueur not in choix_possibles:
            print("⛔ Choix invalide. Veuillez choisir : pierre, papier ou ciseaux.")
            continue
        
        # Choix de l'ordinateur
        ordinateur = random.choice(choix_possibles)
        
        print(f"Vous avez choisi : {joueur}")
        print(f"L'ordinateur a choisi : {ordinateur}")
        
        # Déterminer le gagnant de la partie
        resultat = ""
        if joueur == ordinateur:
            resultat = "Égalité"
            donnees_joueur['scores']['egalites'] += 1
            print("🟡 Égalité !")
        elif (joueur == "pierre" and ordinateur == "ciseaux") or \
             (joueur == "papier" and ordinateur == "pierre") or \
             (joueur == "ciseaux" and ordinateur == "papier"):
            resultat = "Victoire"
            donnees_joueur['scores']['victoires'] += 1
            print("🎉 Vous avez gagné contre l'ordinateur !")
        else:
            resultat = "Défaite"
            donnees_joueur['scores']['defaites'] += 1
            print("😔 L'ordinateur gagne !")
        
        # Enregistrer la partie
        donnees_joueur['parties'].append({
            "joueur": joueur,
            "ordinateur": ordinateur,
            "resultat": resultat
        })
        
        tours_restants -= 1
        if tours_restants > 0:
            print(f"⏳ Il reste {tours_restants} tour(s).")
        
        # Afficher le score après chaque partie
        afficher_score(donnees_joueur['scores'])
    
    # Fin des 5 tours, afficher le gagnant
    print(f"\nMerci d'avoir joué, {nom_joueur} !")
    determiner_gagnant_global(nom_joueur, donnees_joueur['scores'])
    sauvegarder_donnees(donnees)
    print("✅ Résultats enregistrés dans resultats_pierre_papier_ciseaux.json")

# Lancer le jeu
if __name__ == "__main__":
    jouer_pierre_papier_ciseaux()