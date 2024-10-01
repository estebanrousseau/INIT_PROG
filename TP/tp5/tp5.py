def mystere(liste, valeur):
    """renvoie l'indice de du 4ème nombre egal au nombre entrée en paramètre 

    Args:
        liste (list): liste de nombres
        valeur (int): nombre entier 

    Returns:
        [int]: indice du 4éme nombre egal au nombre entrée en paramètre 
    """
    xxx = 0
    yyy = 0
    #xxx contient le nombre de valeur parcourue 
    #yyy contient le nombre de valeur de la liste egale à la valeur rentrée en paramètre 
    for elem in liste:
        if elem == valeur:
            yyy += 1
            if yyy > 3:
                return xxx # s'éxecute quand yyy > 3 donc quand 4 valeurs de la liste sont egaux à la valeur rentrée en paramètre 
        xxx += 1
    return None


def mystere_i(liste, valeur):
    """renvoie l'indice de du 4ème nombre egal au nombre entrée en paramètre 

    Args:
        liste (list): liste de nombres
        valeur (int): nombre entier 

    Returns:
        [int]: indice du 4éme nombre egal au nombre entrée en paramètre 
    """
    yyy = 0
    #xxx contient le nombre de valeur parcourue 
    #yyy contient le nombre de valeur de la liste egale à la valeur rentrée en paramètre 
    for i in range(len(liste)):
        if liste[i] == valeur:
            yyy += 1
            if yyy > 3:
                return i # s'éxecute quand yyy > 3 donc quand 4 valeurs de la liste sont egaux à la valeur rentrée en paramètre 
       
    return None




mystere([12, 5, 8, 48, 12, 418, 185, 17, 5, 87], 20)




#exercice 2 

def nb_in_str(car):
    """renvoie l'indice du premier nombre dans la chaine de caractère

    Args:
        car (str): 

    Returns:
        i (int): 
    """

    for i in range(len(car)):
        if car[i] in '0123456789':
            return i 
    return None    

def test_nb_in_str():
    assert nb_in_str('ehferghfyugeryugferughfyugerqyugryug') is None
    assert nb_in_str('1hferghfyugeryugferughfyugerqyugryug') == 0
    assert nb_in_str('hjgjhgfty1') == 9
    assert nb_in_str('1') == 0



# --------------------------------------
# Exemple de villes avec leur population
# --------------------------------------
liste_villes = ["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux",
                "Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon"]
population = [45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238,
              136463,  25725]



def pop_ville(lst_v, lst_p, ville):
    """renvoie le nombre de population d'une ville si elle existe

    Args:
        lst_v (list): 
        lst_p (list): 
        ville (list): 

    Returns:
        _int : population de la ville attendue
    """
    res = None
    for i in range(len(lst_v)):
        if lst_v[i] == ville :
            res = lst_p[i]
    return res         

def test_pop_ville():
    assert pop_ville(liste_villes, population,'Chartres' ) == 38426
    assert pop_ville(liste_villes, population,'Blois' ) == 45871
    assert pop_ville(liste_villes, population,'Vierzon' ) == 25725
    assert pop_ville(liste_villes, population,'Tours' ) == 136463



def croissant(lst):
    """trouve si la liste est croissante 

    Args:
        lst (list): 

    Returns:
        bool: 
    """
    prec = lst[0]
    res = True
    for i in range(len(lst)):
        if lst[i] < prec :
            res = False
        prec = lst[i] 

    return  res        

def test_croissant():
    assert croissant([1,2,3,4,5,6,7,8,9])
    assert croissant([1])
    assert not croissant([1,2,3,4,5,6,5,8,9])
    assert not croissant([2,1])


def depasse_som_liste(lst, val):
    """ revoie True si la valeur entrée en paramètre depasse la somme totale de la liste

    Args:
        lst (list):
        val (int): 
    Returns:
        bool: 
    """
    if lst == []:
        return False
    
    som = 0
    for nb in lst :
        som += nb 
    return som < val 

def test_depasse_som_liste():
    assert depasse_som_liste([1,2,3,4], 11)
    assert depasse_som_liste([1,2,3,4,5], 16)
    assert not depasse_som_liste([1,2,3,4], 10)
    assert not depasse_som_liste([], 18)


def email(car):
    if car[0] == '@':
        return False
    
    elif car[-1] == '.':
        return False
    
    a_plus_point = False
    arobase = 0 

    for i in range(1, len(car) - 2):
        if car[i] == ' ':
            return False
        
        elif car[i] == '@' and car[i + 1] == '.':
            a_plus_point = True

        if car[i] == '@' :
            arobase += 1  

        if arobase == 2 :
            return False      

    return a_plus_point        

def test_email():
    assert email('jean.eude@.fr')
    assert not email('jean.eude@fr')
    assert not email('jean.eude@.fr.')
    assert not email('@jean.eude@.fr')
    assert not email('@jean.eude.fr')
    assert not email('j@ean.eude.fr')

# ---------------------------------------
# Exemple de scores
# ---------------------------------------
scores = [352100, 325410, 312785, 220199, 127853]
joueurs = ['Batman', 'Robin', 'Batman', 'Joker', 'Batman']
