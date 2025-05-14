import random
import json
import os

FICHIER_HISTORIQUE = "historique.json"

def charger_historique():
    if os.path.exists(FICHIER_HISTORIQUE):
        with open(FICHIER_HISTORIQUE, "r") as f:
            return json.load(f)
    else:
        return {"meilleur_score": None, "parties": []}

def sauvegarder_historique(historique):
    with open(FICHIER_HISTORIQUE, "w") as f:
        json.dump(historique, f, indent=4)

def choisir_difficulte():
    print("\n=== 🎯 Jeu de devinette ===")
    print("Choisis un niveau de difficulté :")
    print("1. Facile (1 à 10, 5 essais)")
    print("2. Normal (1 à 50, 7 essais)")
    print("3. Difficile (1 à 100, 5 essais)")

    while True:
        choix = input("👉 Entrez 1, 2 ou 3 : ")
        if choix == "1":
            return "Facile", 1, 10, 5
        elif choix == "2":
            return "Normal", 1, 50, 7
        elif choix == "3":
            return "Difficile", 1, 100, 5
        else:
            print("⛔ Choix invalide. Réessaie.")

def jouer_partie(historique):
    niveau, min_val, max_val, essais_max = choisir_difficulte()
    secret = random.randint(min_val, max_val)
    essais = 0
    gagne = False

    print(f"\n🔢 Devine le nombre entre {min_val} et {max_val} ! Tu as {essais_max} essais.")

    while essais < essais_max:
        try:
            guess = int(input(f"Essai {essais + 1} : "))
        except ValueError:
            print("⛔ Entrez un nombre entier valide.")
            continue

        essais += 1

        if guess < secret:
            print("🔽 Trop petit !")
        elif guess > secret:
            print("🔼 Trop grand !")
        else:
            print(f"🎉 Bravo ! Tu as trouvé le nombre {secret} en {essais} essais.")
            gagne = True
            if historique["meilleur_score"] is None or essais < historique["meilleur_score"]:
                historique["meilleur_score"] = essais
                print("🌟 Nouveau meilleur score !")
            break

    if not gagne:
        print(f"💀 Tu as perdu. Le nombre était : {secret}")

    # Enregistrer la partie
    historique["parties"].append({
        "niveau": niveau,
        "nombre": secret,
        "essais": essais,
        "réussi": gagne
    })

    sauvegarder_historique(historique)

def afficher_historique(historique):
    parties = historique["parties"]
    if not parties:
        print("📭 Aucun historique pour l’instant.")
        return
    print("\n📜 Historique des parties :")
    for i, partie in enumerate(parties, 1):
        status = "✅ Gagné" if partie['réussi'] else "❌ Perdu"
        print(f"{i}. Niveau : {partie['niveau']} | Nombre : {partie['nombre']} | Essais : {partie['essais']} | {status}")

def jeu_principal():
    historique = charger_historique()

    while True:
        jouer_partie(historique)

        print(f"\n🏆 Meilleur score (moins d’essais) : {historique['meilleur_score'] if historique['meilleur_score'] else 'Aucun'}")
        afficher_historique(historique)

        rejouer = input("\n🔁 Veux-tu rejouer ? (o/n) : ").lower()
        if rejouer != 'o':
            print("👋 Merci d’avoir joué ! À bientôt.")
            break

# Lancer le jeu
jeu_principal()
