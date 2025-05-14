import json
import os

FICHIER_IMC = "imc_resultats.json"

def interpretation_imc(imc):
    if imc < 18.5:
        return "Maigreur"
    elif imc < 25:
        return "Corpulence normale"
    elif imc < 30:
        return "Surpoids"
    elif imc < 35:
        return "Obésité modérée"
    elif imc < 40:
        return "Obésité sévère"
    else:
        return "Obésité morbide"

def charger_donnees():
    if os.path.exists(FICHIER_IMC):
        with open(FICHIER_IMC, "r") as f:
            return json.load(f)
    return []

def sauvegarder_donnees(donnees):
    with open(FICHIER_IMC, "w") as f:
        json.dump(donnees, f, indent=4)

def calculer_imc():
    print("=== 🧮 Calculatrice d'IMC ===")
   
    try:
        nom = input("🧑 Entrez votre nom : ")
        
        # Gestion du poids avec remplacement de la virgule par un point
        poids_input = input("⚖️ Entrez votre poids (en kg) : ")
        poids_input = poids_input.replace(',', '.')
        poids = float(poids_input)
        
        # Gestion de la taille avec remplacement de la virgule par un point
        taille_input = input("📏 Entrez votre taille (en mètres) : ")
        taille_input = taille_input.replace(',', '.')
        taille = float(taille_input)
        
        print(f"Poids saisi: {poids} kg")
        print(f"Taille saisie: {taille} m")
        
    except ValueError:
        print("⛔ Entrée invalide. Veuillez entrer des nombres valides.")
        return
    
    if poids <= 0 or taille <= 0:
        print("⛔ Le poids et la taille doivent être positifs.")
        return
        
    # Vérification supplémentaire pour la taille
    if taille > 3:  # Si la taille est supérieure à 3 mètres, c'est probablement en centimètres
        print("⚠️ La taille semble très grande. Elle doit être en mètres et non en centimètres.")
        print("⚠️ Par exemple, pour 1m75, entrez 1.75 ou 1,75")
        print("⚠️ Conversion automatique de centimètres en mètres...")
        taille = taille / 100
        print(f"Nouvelle taille utilisée: {taille} m")
    
    imc = poids / (taille ** 2)
    interpretation = interpretation_imc(imc)
    
    print(f"\n💡 {nom}, votre IMC est : {imc:.2f}")
    print(f"📌 Interprétation : {interpretation}")
    
    # Charger l'ancien historique
    donnees = charger_donnees()
    
    # Ajouter la nouvelle entrée
    donnees.append({
        "nom": nom,
        "poids_kg": poids,
        "taille_m": taille,
        "imc": round(imc, 2),
        "interpretation": interpretation
    })
    
    # Sauvegarder
    sauvegarder_donnees(donnees)
    print("✅ Résultat enregistré dans imc_resultats.json")

# Lancer le programme correctement
if __name__ == "__main__":
    calculer_imc()