def afficher_menu():
    print("\n=== Convertisseur d'unités ===")
    print("1. Mètres -> Kilomètres")
    print("2. Kilomètres -> Mètres")
    print("3. Mètres -> Centimètres")
    print("4. Mètres -> Millimètres")
    print("5. Mètres -> Pouces")
    print("6. Mètres -> Pixels (96 dpi)")
    print("7. Quitter")

def convertir():
    while True:
        afficher_menu()
        choix = input("👉 Choisissez une conversion (1-7) : ")

        if choix == "1":
            m = float(input("Entrez la valeur en mètres : "))
            print(f"{m} m = {m / 1000} km")
        elif choix == "2":
            km = float(input("Entrez la valeur en kilomètres : "))
            print(f"{km} km = {km * 1000} m")
        elif choix == "3":
            m = float(input("Entrez la valeur en mètres : "))
            print(f"{m} m = {m * 100} cm")
        elif choix == "4":
            m = float(input("Entrez la valeur en mètres : "))
            print(f"{m} m = {m * 1000} mm")
        elif choix == "5":
            m = float(input("Entrez la valeur en mètres : "))
            print(f"{m} m = {m * 39.3701:.2f} pouces")
        elif choix == "6":
            m = float(input("Entrez la valeur en mètres : "))
            pixels = m * 39.3701 * 96
            print(f"{m} m = {pixels:.0f} pixels (à 96 DPI)")
        elif choix == "7":
            print("👋 Fin du programme.")
            break
        else:
            print("⛔ Choix invalide. Réessaie.")

# Lancer le convertisseur
convertir()
