#Generateur de mots de passe
import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation


    characters = letters
    if numbers:
        characters += digits

    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True

        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = meets_criteria and has_number

        if special_characters:
            meets_criteria = meets_criteria and has_special
    
    return pwd

min_length = int(input("Entrez le nombre de caractere : "))
has_number = input("Voullez vous inclure les nombres dans votre mot de passe (y/n)").lower() == "y"
has_special = input("Voullez vous inclure les caractères speciaux (y/n)").lower() == "y"
pwd = generate_password(min_length, has_number, has_special)
print("Le mot de passe génerer est : ", pwd)
