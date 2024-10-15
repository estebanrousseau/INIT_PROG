# --------------------------------------
# DONNEES
# --------------------------------------

# exemple de liste d'oiseaux observables
oiseaux = [("Merle", "Turtidé"), ("Moineau", "Passereau"), ("Mésange", "Passereau"),
           ("Pic vert", "Picidae"), ("Pie", "Corvidé"), ("Pinson", "Passereau"),
           ("Rouge-gorge", "Passereau"), ("Tourterelle", "Colombidé")] 

# exemples de listes de comptage ces listes ont la même longueur que oiseaux
comptage1 = [2, 5, 0, 1, 2, 0, 3, 5]
comptage2 = [2, 1, 3, 0, 0, 3, 5, 1]
comptage3 = [0, 0, 4, 3, 2, 1, 2, 4]

# exemples de listes d'observations. Notez que chaque liste correspond à la liste de comptage de
# même numéro
observations1 = [("Merle", 2), ("Moineau", 5), ("Pic vert", 1), ("Pie", 2),
                 ("Rouge-gorge", 3), ("Tourterelle", 5)]

observations2 = [("Merle", 2), ("Mésange", 1), ("Moineau", 3),
                 ("Pinson", 3), ("Tourterelle", 5), ("Rouge-gorge", 1)]

observations3 = [("Mésange", 4), ("Pic vert", 3), ("Pie", 2), ("Pinson", 1),
                 ("Rouge-gorge", 2), ("Tourterelle", 4)]


# --------------------------------------
# FONCTIONS
# --------------------------------------

def oiseau_le_plus_observe(liste_observations):
    """ recherche le nom de l'oiseau le plus observé de la liste
        (si il y en a plusieur on donne le 1er trouve)

    Args:
        liste_observations (list): une liste de tuples (nom_oiseau, nb_observes)

    Returns:
        str: l'oiseau le plus observé (None si la liste est vide)
    """
    if liste_observations == []:
        res = None
    else:    
        res = liste_observations[0]
        for observation in liste_observations:
            if observation[1] > res[1]:
                res  = observation
        res = res[0]        
    return res



#--------------------------------------
# PROGRAMME PRINCIPAL
#--------------------------------------

# afficher_graphique_observation(construire_liste_observations(oiseaux, comptage3))
# observes = saisie_observations(oiseaux)
# afficher_graphique_observation(observes)
# afficher_observations(oiseaux, observes)


def oiseau_le_plus_observe_i(liste_observations):
    """ recherche le nom de l'oiseau le plus observé de la liste
        (si il y en a plusieur on donne le 1er trouve)

    Args:
        liste_observations (list): une liste de tuples (nom_oiseau, nb_observes)

    Returns:
        str: l'oiseau le plus observé (None si la liste est vide)
    """
    if liste_observations == []:
        res = None
    else:    
        res = liste_observations[0]
        for observation in range(1, len(liste_observations)):
            if observation[1] > res[1]:
                res  = observation
        res = res[0]        
    return res




#-----------------------------------------------------------------------------------------------
#exercice 2 
#-----------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------
#2.1
#-----------------------------------------------------------------------------------------------

def caracteristique(lst_oiseau, nom):
    """permet de retrouver les caractéristiques (nom,famille) d’un oiseau
       dans une liste d’oiseaux à partir de son nom

    Args:
        lst_oiseau (list): 
        nom (str): nom d'oiseau

    Returns:
        _type_: _description_

    invariant :
        l'oiseau n'a pas été trouvé    
    """
    for woiso in lst_oiseau :
        if woiso[0] == nom :
            return woiso
    return None 


#-----------------------------------------------------------------------------------------------
#2.2
#-----------------------------------------------------------------------------------------------

def meme_fammille(lst_oiseau, nom):
    """trouve tous les oiseaux appartenant à la famille entré en parametre 

    Args:
        lst_oiseau (list): liste de tuple oiseau,famille
        nom (str): nom de famille  

    Returns:
        list: mliste de tout les oiseaux
    invariant:
        lst_final contient tout les oiseaux appartenant au nom de famille entré en parametre 
    """
    lst_final = []
    for woiso in lst_oiseau:
        if woiso[1] == nom :
            lst_final.append(woiso[0])
    return lst_final        

#-------------------------------------------------------------------------------------------------
#exercice 3
#-------------------------------------------------------------------------------------------------

def verif_observation(lst):
    """verifie si une liste d'observation est construite correctement 

    Args:
        lst (list): liste d'observation

    Returns:
        bool: vrai si elle est bien construite et faux sinon
    invariant:
        la liste d'observation est bien construite 
    """
    if lst == []:
        return False
    else :
        for woiso in lst :
            if not type(woiso[1]) is int : 
                return False
        return True    
    
#------------------------------------------------
# #3.2
# -----------------------------------------------

def max_oiseaux(lst):
    """donne le plus grand nombre de spécimens observés dans une liste
        d’observations

    Args:
        lst (list): liste d'observation

    Returns:
        int: maximum d'appartion d'oiseaux et None si la liste est vide
    """
    if lst != []:
        maxi = lst[0][1]
        for woiso in lst :
            if woiso[1] > maxi :
                maxi = woiso[1]
        return maxi            