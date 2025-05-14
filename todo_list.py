# To-Do List en console

taches = []

def afficher_menu():
    print("\n=== TO-DO LIST ===")
    print("1. Afficher les tâches")
    print("2. Ajouter une tâche")
    print("3. Marquer une tâche comme faite")
    print("4. Supprimer une tâche")
    print("5. Quitter")

def afficher_taches():
    if not taches:
        print("📭 Aucune tâche pour l’instant.")
    else:
        print("\n📋 Liste des tâches :")
        for i, tache in enumerate(taches, 1):
            status = "✅" if tache['faite'] else "❌"
            print(f"{i}. {tache['texte']} {status}")

def ajouter_tache():
    texte = input("📝 Entrez la tâche : ").strip()
    if texte:
        taches.append({'texte': texte, 'faite': False})
        print("➕ Tâche ajoutée.")
    else:
        print("⛔ Texte de tâche vide.")

def marquer_faite():
    afficher_taches()
    try:
        num = int(input("Entrez le numéro de la tâche à cocher : "))
        if 1 <= num <= len(taches):
            taches[num - 1]['faite'] = True
            print("☑️ Tâche marquée comme faite.")
        else:
            print("⛔ Numéro invalide.")
    except ValueError:
        print("⛔ Entrée non valide.")

def supprimer_tache():
    afficher_taches()
    try:
        num = int(input("Entrez le numéro de la tâche à supprimer : "))
        if 1 <= num <= len(taches):
            supprimee = taches.pop(num - 1)
            print(f"🗑️ Tâche supprimée : {supprimee['texte']}")
        else:
            print("⛔ Numéro invalide.")
    except ValueError:
        print("⛔ Entrée non valide.")

# Boucle principale
while True:
    afficher_menu()
    choix = input("👉 Choisissez une option (1-5) : ")

    if choix == "1":
        afficher_taches()
    elif choix == "2":
        ajouter_tache()
    elif choix == "3":
        marquer_faite()
    elif choix == "4":
        supprimer_tache()
    elif choix == "5":
        print("👋 Au revoir !")
        break
    else:
        print("⛔ Option invalide.")
