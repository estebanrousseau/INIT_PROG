# TP8 B - Manipuler des listes, ensembles et dictionnaires
# exercice 1 
#1.1 
# jean a 12 vaches, 17 cochons et 3 veaux 
# l'autre n'a rien 

mon_troupeau = {
    'vache' : 14 ,
    'mouton' : 2 ,
    'chat' : 4 
}





def total_animaux(troupeau):
    """ Calcule le nombre total d'animaux dans un troupeau

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        int: le nombre total d'animaux dans le troupeau
    """
    tot = 0 
    for val in troupeau.values():
        tot += val 
    return tot     


def tous_les_animaux(troupeau):
    """ Détermine l'ensemble des animaux dans un troupeau

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        set: l'ensemble des animaux du troupeau
    """
    res = set()
    for animal in troupeau:
        res.add(animal)
    return res     


def specialise(troupeau):
    """ Vérifie si le troupeau contient 30 individus ou plus d'un même type d'animal 

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        bool: True si le troupeau contient 30 (ou plus) individus d'un même type d'animal,
        False sinon 
    """
    for val in troupeau.values():
        if val >= 30 :
            return True
    return False 


def le_plus_represente(troupeau):
    """ Recherche le nom de l'animal qui a le plus d'individus dans le troupeau
    
    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        str: le nom de l'animal qui a le plus d'individus  dans le troupeau
        None si le troupeau est vide) 
    
    """
    res = None 
    maxi = 0 
    for cle, val in troupeau.items():
        if val > maxi :
            maxi = val 
            res = cle 
    return res         






def reunion_troupeaux(troupeau1, troupeau2):
    """ Simule la réunion de deux troupeaux

    Args:
        troupeau1 (dict): un dictionnaire modélisant un premier troupeau {nom_animaux: nombre}
        troupeau2 (dict): un dictionnaire modélisant un deuxième troupeau        

    Returns:
        dict: le dictionnaire modélisant la réunion des deux troupeaux    
    """
    troupeau_reunion = {}
    for cle, val in troupeau1.items():
        troupeau_reunion[cle] = val
    
    for cle, val in troupeau2.items():

        if cle in troupeau_reunion :
            troupeau_reunion[cle] += val 

        else :
            troupeau_reunion[cle] = val 
    return troupeau_reunion                

def quantite_suffisante(troupeau):
    """ Vérifie si le troupeau contient au moins 5 individus de chaque type d'animal

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        bool: True si le troupeau contient au moins 5 individus de chaque type d'animal
        False sinon    
    """
    for val in troupeau.values():
        if val < 5 :
            return False
    return True







