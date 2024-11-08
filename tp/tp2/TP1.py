#print('bienvenue à l IUT 0')

def exemple_debug(x, y):
    nb = 15
    ch = "cou"
    nb = x+y
    return ch*2

# programme principal
#print(exemple_debug(5, 6))

"""def fonction1(x):
    a = 12
    a = 3+y
    return a
#print(fonction1(23))"""

def fonction2(x):
    a = 12
    a = 3+x
    A = a/2
    b = a
    a = 5
    b = b+1
    return a
#print(fonction2(5))

#exercice 5

def algo_1(a, b, c, d):
    """trouve le minimun parmi les nombres entrés en parametre

    Args:
        a (int)
        b (int)
        c (int)
        d (int)
    """    

    if a < b :
        res = a

    else :
        res = b   

    if c < res :
        res = c    
          
    if d < res :
        res = d

    return res     


def algo_2(car):
    """renvoie si i y a plus de voyelle ou de consonne dans un mot

    Args:
        car (str): 

    Returns:
        bool : renvoie si c'est vrai ou faux
    """
    res = 0
    for lettre in car :
        if lettre in 'aeiuoy':
            res += 1 
        else:
            res -= 1 
    return res > 0  
  
def test_algo_2():
    assert(algo_2("auo")) == True 
    assert(algo_2("trgoo")) == False

#exercice 6 :
# 1. les données d'entrer sont sexe, temps, course_gagné, champion 
# 2. qualifié: 11s et 4 fois gagnant / non qualifié: 16s et 4 fois gagnant

def est_qualifie(sexe, tps, course_g, champion):
    """_summary_

    Args:
        sexe (str): 
        tps (_int_): 
        course_g (int): _
        champion (bool): 
    Returns:
        bool : renvoie si l'athlete est qualifie a la competition
    """


    if sexe not in "fm":
        raise(ValueError("le sexe doit etre soit f soit m "))

    elif sexe == "f" and tps < 15 and course_g >= 3 :
        res =  True
    
    elif sexe == "m" and tps < 12 and course_g >= 3 :
        res =  True
    
    elif champion :
        res =  True

    else :
        res = False 

    return res

def test_est_qualifie():
    assert(est_qualifie('f', 15, 2, True)) == True
    assert(est_qualifie('f', 15, 2, False)) == False




#exrecice 7 
# 1. c'est la vitesse de conducteur , vitesse autorisé, recidive
# 2. plus de 20km/h : 68 euros , -1 point , aucun 

def depassement_vitesse(vistesse_conducteur , vitesse_autoriser, recidive):
    """ calcul les sanctions en fonctions du depassements de vitesse

    Args:
        vistesse_conducteur (int): 
        vitesse_autoriser (_int_): 
        recidive (bool): 

    Returns:
        _amande, point, retrait : int, int, int,
    """

    depassement = vistesse_conducteur - vitesse_autoriser


    if depassement > 49 :
        if recidive :
            amande, point, retrait = 3750, 6, 3 
        else     :
            amande, point, retrait = 1500, 6, 3 


    elif depassement > 39 :
        amande, point, retrait = 135, 4, 3 


    elif depassement > 29 :
        amande, point, retrait = 135, 3, 3

    elif depassement > 19 :
        amande, point, retrait = 135, 2, 0  

    elif depassement > 0  :
        if vitesse_autoriser <= 50:
            amande, point, retrait = 135, 1, 0  
        else:
            amande, point, retrait = 68, 2, 0      

   
    return amande,point,retrait
        
def test_depassement_vitesse():
    assert(depassement_vitesse(180, 130, False)) == (1500, 6, 3)
