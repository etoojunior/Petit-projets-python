import random
import time
import json
import os

class QuizCultureGenerale:
    def __init__(self):
        self.nom_joueur = ""
        self.score = 0
        self.fichier_scores = "scores_quiz.json"
        self.questions = [
            # Questions générales
            {
                "question": "Quelle est la capitale de l'Australie ?",
                "options": ["Sydney", "Melbourne", "Canberra", "Perth"],
                "reponse": "Canberra"
            },
            {
                "question": "Qui a peint La Joconde ?",
                "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
                "reponse": "Leonardo da Vinci"
            },
            {
                "question": "En quelle année a eu lieu la Révolution française ?",
                "options": ["1769", "1789", "1799", "1809"],
                "reponse": "1789"
            },
            {
                "question": "Quel est le plus grand océan du monde ?",
                "options": ["Océan Atlantique", "Océan Indien", "Océan Arctique", "Océan Pacifique"],
                "reponse": "Océan Pacifique"
            },
            {
                "question": "Qui a écrit 'Les Misérables' ?",
                "options": ["Albert Camus", "Victor Hugo", "Émile Zola", "Gustave Flaubert"],
                "reponse": "Victor Hugo"
            },
            {
                "question": "Quel est l'élément chimique le plus abondant dans l'univers ?",
                "options": ["Oxygène", "Carbone", "Hydrogène", "Hélium"],
                "reponse": "Hydrogène"
            },
            {
                "question": "Quelle est la plus haute montagne du monde ?",
                "options": ["Mont Blanc", "Mont Kilimandjaro", "Mont Everest", "K2"],
                "reponse": "Mont Everest"
            },
            {
                "question": "Combien de planètes compte notre système solaire ?",
                "options": ["7", "8", "9", "10"],
                "reponse": "8"
            },
            {
                "question": "Quel pays a remporté le plus de Coupes du Monde de football ?",
                "options": ["Allemagne", "Italie", "Argentine", "Brésil"],
                "reponse": "Brésil"
            },
            {
                "question": "Quelle est la capitale du Japon ?",
                "options": ["Pékin", "Séoul", "Tokyo", "Bangkok"],
                "reponse": "Tokyo"
            },
            # Questions sur le Cameroun
            {
                "question": "Quelle est la capitale du Cameroun ?",
                "options": ["Douala", "Yaoundé", "Bamenda", "Garoua"],
                "reponse": "Yaoundé"
            },
            {
                "question": "En quelle année le Cameroun a-t-il obtenu son indépendance ?",
                "options": ["1960", "1957", "1962", "1970"],
                "reponse": "1960"
            },
            {
                "question": "Comment appelle-t-on les habitants du Cameroun ?",
                "options": ["Camerounais", "Camerouniens", "Camerounois", "Camerounistes"],
                "reponse": "Camerounais"
            },
            {
                "question": "Quel est le surnom de l'équipe nationale de football du Cameroun ?",
                "options": ["Les Éléphants", "Les Lions Indomptables", "Les Aigles", "Les Panthères"],
                "reponse": "Les Lions Indomptables"
            },
            {
                "question": "Quelle est la montagne la plus élevée du Cameroun ?",
                "options": ["Mont Cameroun", "Mont Oku", "Mont Manengouba", "Mont Mandara"],
                "reponse": "Mont Cameroun"
            },
            {
                "question": "Combien de langues officielles compte le Cameroun ?",
                "options": ["1", "2", "3", "4"],
                "reponse": "2"
            },
            {
                "question": "Quel est le plus grand lac naturel du Cameroun ?",
                "options": ["Lac Tchad", "Lac Nyos", "Lac Ossa", "Lac Barombi Mbo"],
                "reponse": "Lac Tchad"
            },
            {
                "question": "Quelle est la principale exportation agricole du Cameroun ?",
                "options": ["Café", "Cacao", "Bananes", "Coton"],
                "reponse": "Cacao"
            },
            {
                "question": "Quel célèbre footballeur camerounais a remporté la médaille d'or olympique en 2000 ?",
                "options": ["Roger Milla", "Samuel Eto'o", "Patrick Mboma", "Rigobert Song"],
                "reponse": "Samuel Eto'o"
            },
            {
                "question": "Quel fleuve traverse la ville de Douala au Cameroun ?",
                "options": ["Le Wouri", "Le Sanaga", "Le Congo", "Le Nyong"],
                "reponse": "Le Wouri"
            }
        ]
    
    def charger_scores(self):
        if os.path.exists(self.fichier_scores):
            try:
                with open(self.fichier_scores, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []
    
    def sauvegarder_score(self):
        scores = self.charger_scores()
        
        # Créer une nouvelle entrée de score
        nouvelle_entree = {
            "nom": self.nom_joueur,
            "score": self.score,
            "max_score": 10,  # On pose 10 questions maintenant
            "date": time.strftime("%Y-%m-%d %H:%M:%S"),
            "pourcentage": (self.score / 10) * 100
        }
        
        scores.append(nouvelle_entree)
        
        # Sauvegarder dans le fichier JSON
        with open(self.fichier_scores, 'w') as f:
            json.dump(scores, f, indent=4)
        
        print(f"\n✅ Score enregistré dans {self.fichier_scores}")
    
    def afficher_meilleurs_scores(self):
        scores = self.charger_scores()
        
        if not scores:
            print("\nAucun score enregistré pour le moment.")
            return
        
        # Trier les scores par ordre décroissant
        scores_tries = sorted(scores, key=lambda x: x["score"], reverse=True)
        
        print("\n📊 TABLEAU DES MEILLEURS SCORES 📊")
        print("-" * 50)
        print(f"{'Nom':<15} {'Score':<8} {'Date':<20} {'%':<5}")
        print("-" * 50)
        
        # Afficher les 5 meilleurs scores
        for i, score in enumerate(scores_tries[:5], 1):
            print(f"{score['nom']:<15} {score['score']}/{score['max_score']:<8} {score['date']:<20} {score['pourcentage']}%")
    
    def afficher_accueil(self):
        print("\n" + "=" * 60)
        print("🧠  QUIZ DE CULTURE GÉNÉRALE ET DU CAMEROUN  🧠")
        print("=" * 60)
        print("Bienvenue dans ce quiz de culture générale et sur le Cameroun !")
        
        # Demander le nom du joueur
        self.nom_joueur = input("\nEntrez votre nom : ")
        while not self.nom_joueur.strip():
            print("⚠️ Veuillez entrer un nom valide.")
            self.nom_joueur = input("Entrez votre nom : ")
        
        print(f"\nBonjour {self.nom_joueur} ! Prêt(e) à tester vos connaissances ?")
        print("Répondez aux questions en entrant le numéro de votre choix.")
        
    def poser_question(self, question_data):
        print("\n📝 " + question_data["question"])
        
        # Mélanger les options pour chaque question
        options = question_data["options"].copy()
        random.shuffle(options)
        
        # Mémoriser la position de la bonne réponse
        reponse_correcte_index = options.index(question_data["reponse"]) + 1
        
        # Afficher les options
        for i, option in enumerate(options, 1):
            print(f"   {i}. {option}")
        
        # Obtenir la réponse de l'utilisateur
        while True:
            try:
                choix = int(input("\nVotre réponse (1-4) : "))
                if 1 <= choix <= 4:
                    break
                else:
                    print("⚠️ Veuillez entrer un nombre entre 1 et 4.")
            except ValueError:
                print("⚠️ Veuillez entrer un nombre valide.")
        
        # Vérifier la réponse
        if choix == reponse_correcte_index:
            print("✅ Correct ! Bien joué !")
            return True
        else:
            print(f"❌ Incorrect. La bonne réponse était : {question_data['reponse']}")
            return False
    
    def demarrer_quiz(self):
        self.afficher_accueil()
        
        # Attendre que l'utilisateur soit prêt
        input("\nAppuyez sur Entrée pour commencer...")
        
        # Mélanger les questions pour chaque partie
        questions_melangees = self.questions.copy()
        random.shuffle(questions_melangees)
        
        # Limiter à 10 questions par partie
        questions_partie = questions_melangees[:10]
        
        # Poser chaque question
        for i, question in enumerate(questions_partie, 1):
            print(f"\n--- Question {i}/10 ---")
            if self.poser_question(question):
                self.score += 1
            
            # Petite pause entre les questions
            if i < len(questions_partie):
                time.sleep(1)
        
        # Afficher le résultat final
        self.afficher_resultat()
    
    def afficher_resultat(self):
        print("\n" + "=" * 60)
        print(f"📊 Résultat final pour {self.nom_joueur} : {self.score}/10")
        
        # Message personnalisé selon le score
        if self.score == 10:
            print("🏆 Parfait ! Vous êtes un(e) expert(e) en culture générale et sur le Cameroun !")
        elif self.score >= 7:
            print("👍 Excellent ! Vous avez de très bonnes connaissances !")
        elif self.score >= 5:
            print("👍 Bien joué ! Vous avez de bonnes connaissances générales.")
        else:
            print("📚 Continuez à apprendre, la culture générale s'améliore avec le temps !")
        
        print("=" * 60)
        
        # Sauvegarder le score
        self.sauvegarder_score()
        
        # Afficher les meilleurs scores
        self.afficher_meilleurs_scores()
        
        # Proposer de rejouer
        rejouer = input("\nVoulez-vous rejouer ? (oui/non) : ").lower()
        if rejouer in ["oui", "o", "yes", "y"]:
            self.score = 0
            self.demarrer_quiz()
        else:
            print("\nMerci d'avoir joué au Quiz de Culture Générale ! À bientôt !")

# Lancer le quiz
if __name__ == "__main__":
    quiz = QuizCultureGenerale()
    quiz.demarrer_quiz()