import random

# Liste de mots possibles
mots = ['ordinateur', 'python', 'programmation', 'developpeur', 'intelligence', 'variable', 'souris', 'linux', 'java', 'pixel', 'algorithmique','navigateur', 'framework', 'cryptage', 'terminal', 'compilateur', 'virtualisation', 'cybersecurite', 'systeme' ]

# Choisir un mot aléatoire
mot_a_deviner = random.choice(mots)
lettres_trouvees = ['_' for _ in mot_a_deviner]
lettres_essayer = []
tentatives_restantes = 7

print("🎮 Bienvenue dans le jeu du Pendu !")
print("Le mot contient", len(mot_a_deviner), "lettres.")

# Boucle principale
while tentatives_restantes > 0 and '_' in lettres_trouvees:
    print("\nMot à deviner : ", ' '.join(lettres_trouvees))
    print("Lettres essayées : ", ' '.join(lettres_essayer))
    print("Tentatives restantes :", tentatives_restantes)

    lettre = input("Propose une lettre : ").lower()

    if not lettre.isalpha() or len(lettre) != 1:
        print("⛔ Entrée invalide. Entrez une seule lettre.")
        continue

    if lettre in lettres_essayer:
        print("⚠️ Tu as déjà essayé cette lettre.")
        continue

    lettres_essayer.append(lettre)

    if lettre in mot_a_deviner:
        print("✅ Bien joué ! La lettre est dans le mot.")
        for i in range(len(mot_a_deviner)):
            if mot_a_deviner[i] == lettre:
                lettres_trouvees[i] = lettre
    else:
        print("❌ Mauvais choix.")
        tentatives_restantes -= 1

# Fin du jeu
if '_' not in lettres_trouvees:
    print("\n🎉 Félicitations ! Tu as deviné le mot :", mot_a_deviner)
else:
    print("\n💀 Tu as perdu. Le mot était :", mot_a_deviner)
