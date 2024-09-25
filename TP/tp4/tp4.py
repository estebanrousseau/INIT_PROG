def plus_long_plateau(chaine):
    """recherche la longueur du plus grand plateau d'une chaine
    Args:
        chaine (str): une chaine de caractères

    Returns:
        int: la longueur de la plus grande suite de lettres consécutives égales
    """
    if chaine == '':
        return 0 

    lg_max = 1  # longueur du plus grand plateau déjà trouvé
    lg_actuelle = 1  # longueur du plateau actuel

    for i in range(1, len(chaine)):

        if chaine[i] == chaine[i - 1]:
            lg_actuelle += 1 

            if lg_actuelle > lg_max :
                lg_max = lg_actuelle 

        else:
            lg_actuelle = 1       


    return lg_max


def test_plus_long_plateau():
    assert(plus_long_plateau('')) == 0 
    assert(plus_long_plateau('aaaaaa')) == 6
    assert(plus_long_plateau('abbbaaaabbb')) == 4
    assert(plus_long_plateau('jgiyzyvf')) == 1
    assert(plus_long_plateau('a')) == 1

# --------------------------------------
# Exemple de villes avec leur population
# --------------------------------------
liste_villes = ["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux",
                "Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon"]
population = [45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238, 136463,
              25725]

def ville_plus_peuple(lst_v, lst_p):
    """renvoie la ville la plus peuplé 

    Args:
        lst_v (lst): liste de ville
        lst_p (lst): liste de population
    Raises:
        ValueError: la liste ne doit pas être vide 

    Returns:
        str: la ville la plus peuplé
    """

    if lst_v == []:
        raise ValueError('la liste ne doit pas être vide')
    plus_v = ''
    plus_h = 0 
    for i in range(len(lst_v)):
        if lst_p[i] > plus_h :
            plus_h, plus_v = lst_p[i], lst_v[i]

    return plus_v

def test_plus_pleuple():
    assert(ville_plus_peuple(liste_villes, population)) == 'Tours'
    assert not (ville_plus_peuple(liste_villes, population)) == 'Orleans'


def transforme(chaine):
    """transforme un str en int 

    Args:
        chaine (str): 

    Returns:
        res (int) 
    """
    res = 0 
    for i in range(len(chaine)):
        res = res *10 + int(chaine[i])
    return res     


def test_transforme():
    assert(transforme("")) == 0
    assert(transforme("5")) == 5
    assert(transforme("2354")) == 2354
    assert(transforme("21")) == 21

def recherche_mot(lst, lettre):
    """renvoie les mots qui commencent par la lettre entrée en paramètre

    Args:
        lst (list): liste de mots
        lettre (str): 

    Returns:
        _type_: _description_
    """
    if lst == []:
        return []
    
    return [lst[i]   for i in range(len(lst))   if lst[i][0] == lettre]

def test_recherche_mot():
    assert(recherche_mot(['hello', 'hello'], 'h' )) == ['hello', 'hello']
    assert(recherche_mot(['hello', 'hello'], 'l' )) == []
    assert(recherche_mot(['hello', 'mello'], 'm' )) == ['mello']
    assert(recherche_mot([], 'h' )) == []
    
#exercice 5 

def est_alphabet(str):
    return str in 'azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN' 

def decoupe_mot(chaine):
    """decoupe les mots d'une chaine de caratère

    Args:
        chaine (str): 

    Returns:
        liste_mot (list): liste des mots découpé
    """
    if chaine == '':
        return []
    
    else : 
        liste_mot = []
        mot_temp = ''
        for i in range(len(chaine)):
            if est_alphabet(chaine[i]) :
                mot_temp += chaine[i]

            else:
                if  mot_temp != '':
                    liste_mot.append(mot_temp)
                    mot_temp = ''
        if est_alphabet(chaine[-1]):    
            liste_mot.append(mot_temp)            
        return liste_mot

def test_decoupe_mot():
    assert decoupe_mot('Bonjour tout le monde')  == ['Bonjour', 'tout', 'le', 'monde']     
    assert decoupe_mot('Bonjour ')  == ['Bonjour']      
    assert decoupe_mot('2*4')  == []   
    assert decoupe_mot('')  == [] 

def trouve_mot(chaine, car)    :
    """trouve les mots qui commencent par la lettre donné

    Args:
        chaine (str): chaine de carartère 
        car (str): lettre

    Returns:
        liste_mot (list): 
    """
    return recherche_mot(decoupe_mot(chaine), car)

#def test_trouve_mot('')