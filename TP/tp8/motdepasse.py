# Codé par Papy Force X, jeune padawan de l'informatique

def dialogue_mot_de_passe():
    login = input("Entrez votre nom : ")
    mot_de_passe_correct = False
    while not mot_de_passe_correct :

        mot_de_passe = input("Entrez votre mot de passe : ")

        # je vérifie la longueur
        if len(mot_de_passe) < 8:
            longueur_ok = False
        
        else:
            longueur_ok = True
        # je vérifie s'il y a un chiffre
        chiffre_ok = False
        for lettre in mot_de_passe:
            if lettre.isdigit():
                chiffre_ok = True
        # je vérifie qu'il n'y a pas d'espace
        sans_espace = True
        for lettre in mot_de_passe:
            if lettre == " ":
                sans_espace = False



        # Je gère l'affichage
        if not longueur_ok:
            print("Votre mot de passe doit comporter au moins 8 caractères")

        elif not chiffre_ok:
            print("Votre mot de passe doit comporter au moins un chiffre")

        elif not sans_espace:
            print("Votre mot de passe ne doit pas comporter d'espace")	

        else:
            mot_de_passe_correct = True   

    print("Votre mot de passe est correct")
    return mot_de_passe

#dialogue_mot_de_passe()

#---------------------------------------
# exercice 1 
#---------------------------------------

# pas de docstring sur la fonction
# la fonction depasse 20 lignes 
# la fonction n'est pas testé
# 
# 
# --------------------------------
#              1.2
# --------------------------------
#  

def longueur_ok(car):
    """trouve si une chaine de caractère respecte la règle d'une taille d'au moin 8 caractère 

    Args:
        car (str): entree de l'utilisateur

    Returns:
        bool: vrai si la longueur est superieure à 8 et faux sinon
    """
    return len(car) > 8 

def chiffre_ok(car):
    """trouve si il y a un chiffre dans l'entree d l'utilisateur

    Args:
        car (str): entree de l'utilisateur

    Returns:
        bool : vrai si il y a un chiffre et faux sinon 
    """
    for lettre in car :
        if lettre.isdigit():
            return True
    return False    

def sans_espace(car):
    """trouve si il y a un espace dans une chaine de caractere 

    Args:
        car (str): entree de l'utilisateur

    Returns:
        bool: vrai si il n'y a pas d'espace et faux sinon 
    """
    for lettre in car :
        if lettre == ' ':
            return False
    return True    



def new_dialogue_mdp():

    mdp = False
    while not mdp :
        login = input('entrez votre mot de passe: ')
        if not longueur_ok(login):
            print('la longueur du mot de passse doit est superieur à 8')

        elif not chiffre_ok(login):
            print('le mot de passe doit contenir une chiffre')

        elif not sans_espace(login):
            print('le mot de passe ne doit pas contenir d\'espace')

        else :
            mdp = True     

    return mdp             

new_dialogue_mdp()

#----------------------------------
# exercice2 
#----------------------------------

def trois_app_chif(car):
    """trouve si il y a 3 chiffres dans l'entree d l'utilisateur

    Args:
        car (str): entree de l'utilisateur

    Returns:
        bool : vrai si il y a 3 chiffres et faux sinon 
    """
    cmp = 0
    for lettre in car :
        if lettre.isdigit():
            cmp += 1

        if cmp == 3 :
            return True
    return False    


def chif_suite_ok(car):
    """trouve si il y a 2 chiffre à la suite 

    Args:
        car (str): entree de l'utilisateur

    Returns:
        bool :vrai si il n'y a pas de chiffre à la suite et faux sinon 
    """

    for i in range(1, len(car)):
        if car[i - 1].isdigit() and car[i].isdigit():
            return False
    return True    

def plus_petit_chiffre_ok(car):
    """verifie que le plus petit chiffre n'est pas en double

    Args:
        car (str): entree de l'utilisateur

    Returns:
        bool : vrai si le plus petit chiffre n'est present qu'une fois 
    """
    dico_apparttion = {}

    mini = 10 
    for lettre in car :
        if lettre.isdigit():

            val = int(lettre)
            if val < mini :
                mini = val

            if val not in dico_apparttion:
                dico_apparttion[val] = 0
            else:
                dico_apparttion[val] += 1

    return dico_apparttion[mini] == 1                    