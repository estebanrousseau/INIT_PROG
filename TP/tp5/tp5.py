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
        car (str): une chaine de caractère 

    Returns:
        i (int): indice du premier nombre dans la chaine de caractère
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
        lst_v (list): liste de ville
        lst_p (list): liste de population
        ville (str): une ville

    Returns:
        _int : population de la ville attendue
    """
    res = None
    #res contient le nombre d'habitant d'une ville si elle à été trouver
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
        lst (list): liste de valeur 

    Returns:
        bool: vrai si la liste est croissante et faux dans le cas contraire
    """
    prec = lst[0]
    res = True
    #res dit si la liste parcourue jusqu'à présent est croissante
    #prec contient la valeur de l'avant dernier élément de la liste
    for i in range(1, len(lst)):
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
        lst (list): liste de valeurs
        val (int): une valeur 
    Returns:
        bool: vrai si val depasse la somme de la liste et faux dans le cas contraire 
    """
    if lst == []:
        res = False
    else:
        res = 0
        #som contient la somme des élément de la liste parcourue jusqu'à présent
        for nb in lst :
            res += nb 
        res = res <  val  
    return   res 

def test_depasse_som_liste():
    assert depasse_som_liste([1,2,3,4], 11)
    assert depasse_som_liste([1,2,3,4,5], 16)
    assert not depasse_som_liste([1,2,3,4], 10)
    assert not depasse_som_liste([], 18)


def email(car):
    """test si un email est correct

    Args:
        car (str): un email

    Returns:
        bool: vrai si l'email est correct et faux si il ne l'est pas 
    """

    a_plus_point = False
    arobase = 0 

    if not car[0] == '@' and not car[-1] == '.':
    #arobase contient le nombre d'arobase trouver 
    #a_plus_point dit si un arobase et un point on été trouver sucsessivement
        for i in range(1, len(car) - 2):

            if car[i] == '@' :
                arobase += 1  
                if car[i + 1] == '.':
                    a_plus_point = True

            if arobase == 2 or car[i] == ' ':
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




# exercice 4 

#4.1
 
def meilleur_score(lst_j, lst_s, prenom):
    """trouve le meilleur score d'un joueur

    Args:
        lst_j (list): liste de joueur
        lst_s (list): liste de score
        prenom (str):  prenom d'un joueur

    Returns:
        int: meilleur score du joueur
    """
    if lst_j == [] or lst_s == []:
        res =  None
    else:
        
        res = 0

        #res contient à chaque tour de boucle le 
        #    meilleur score trouver jusqu'à present
        for i in range(len(lst_j)):
            if lst_s[i] > res and lst_j[i] == prenom :
                res = lst_s[i]
    return res             


def test_meilleur_score():
    assert meilleur_score(joueurs, scores, 'Batman') == 352100
    assert meilleur_score(joueurs, scores, 'Joker') == 220199
    assert meilleur_score(joueurs, scores, 'Robin') == 325410
    assert not meilleur_score(joueurs, scores, 'Batman') == 312785



#4.2



def score_decroissant(lst_score):
    """trouve si la liste est decroissante 

    Args:
        lst (list): liste des scores

    Returns:
        bool: vrai si lst_score est decroissante et faux dans le cas contraire
    """
    prec = lst_score[0]

    #prec contient à chaque tour de boucle les 
    #     valeurs sucsessives de la liste
    for i in range(len(lst_score)):
        if lst_score[i] > prec :
            return False 
        prec = lst_score[i] 

    return  True   

def test_score_decroissant():
    assert score_decroissant([9,8,7,6,5,4,3,2,1,])
    assert score_decroissant([1])
    assert not score_decroissant([9,8,7,6,5,4,9,3,2,1])
    assert score_decroissant([2,1])




#4.3


scores = [352100, 325410, 312785, 220199, 127853]
joueurs = ['Batman', 'Robin', 'Batman', 'Joker', 'Batman']  

def apparition_score_joueur(lst_j, prenom):
    """ retourne combien de fois un joueur apparaît dans les meilleurs scores

    Args:
        lst_j (list): liste de joueur
        prenom (list): prnom d'un joueur

    Returns:
        int : nombre d'apparition du joueur dans la liste
    """
    if lst_j == []:
        return None
    else:
        cmp = 0 
        #cmp contient le nombre de fois ou de le  
        #    prenom à été rencontré jusqu'à présent
        for nom in lst_j:
            if nom == prenom:
                cmp += 1
        return cmp        
    
def test_meilleur_score_joueur():
    assert apparition_score_joueur(joueurs, 'Batman') == 3  
    assert apparition_score_joueur(joueurs, 'Robin') == 1 
    assert apparition_score_joueur(joueurs, 'Joker') == 1  
    assert apparition_score_joueur([], 'Batman') == None  




#4.4


def meilleur_classement(lst_j, lst_s, prenom):
    """renvoie le meilleur classement du joueur 

    Args:
        lst_j (list): liste de joueur
        lst_s (list): liste de score
        prenom (list): prenom du joueur

    Returns:
        int: indice de la première apparition du joueur
    """
    meilleur_s = meilleur_score(lst_j, lst_s, prenom)    
    if meilleur_s is None :
        return None

    else:
        for i in range(len(lst_s)):
            if lst_s[i] == meilleur_s:
                return i 

def test_meilleur_classement():
    assert meilleur_classement(joueurs, scores, 'Batman') == 0
    assert meilleur_classement(joueurs, scores, 'Robin') == 1
    assert meilleur_classement(joueurs, scores, 'Joker') == 3
    assert not meilleur_classement(joueurs, scores, 'Batman') == 1


#4.5
def inserer_score(lst_s, score):
    """trouve le bon indice ou inserer le score

    Args:
        lst_s (list):  liste de score
        score (int):  score du joueur

    Returns:
        int: indice de l'endroit ou insérer le score
    """
    if lst_s == []:
        i  = None

    else:
        for i in range(len(lst_s)):
            if score > lst_s[i]:
                return i 
        i += 1     
    return i 

def test_inserer_score():
    assert inserer_score(scores, 314570) == 2
    assert inserer_score(scores, 1) == 5
    assert inserer_score(scores, 9999314570) == 0
    assert inserer_score(scores, 200000) == 4




#4.6

def inserer_joueur_et_score(lst_j, lst_s, prenom, score):
    """modifie la liste de score en ajoutant le score
       au bon endroit dans la liste 

    Args:
        lst_j (list): liste de joueur
        lst_s (list): liste de score
        prenom (str): nouveau prenom à ajouter
        score (int): nouveau score à ajouter
    """
    indice_inserer = inserer_score(lst_s, score)
    lst_j.insert(indice_inserer, prenom)
    lst_s.insert(indice_inserer, score)


def test_inserer_joueur_et_score()  :

    scores = [352100, 325410, 312785, 220199, 127853]
    joueurs = ['Batman', 'Robin', 'Batman', 'Joker', 'Batman']  

    inserer_joueur_et_score(joueurs, scores, 'Eude', 1 )

    assert   scores == [352100, 325410, 312785, 220199, 127853, 1] 
    assert   joueurs == ['Batman', 'Robin', 'Batman', 'Joker', 'Batman', 'Eude'] 

    inserer_joueur_et_score(joueurs, scores, 'Jean', 500000 )

    assert   scores == [500000, 352100, 325410, 312785, 220199, 127853, 1] 
    assert   joueurs == ['Jean', 'Batman', 'Robin', 'Batman', 'Joker', 'Batman', 'Eude'] 

    scores = [352100, 325410, 312785, 220199, 127853]
    joueurs = ['Batman', 'Robin', 'Batman', 'Joker', 'Batman']  
