def somme_lst(lst):
    """calcule la somme d'entier d'une liste

    Args:
        lst (lst): 
    return :
        somme des entier de la liste
    """
    cmp = 0 
    for i in range(len(lst)):
        cmp += lst[i]
    return cmp

def max(lst):
    """trouve la valeur maximun d'une liste 

    Args:
        lst (list): 
    """
    if len(lst) == 0 :
        maxi = None 

    else:
        maxi = lst[0]
        for i in range(1, len(lst)):
            if lst[i] > maxi:
                maxi = lst[i]

    return maxi        

def nb_occ(mot, car):
    """compte de nombres d'occurence d'un caractère dans un mot

    Args:
        mot (str):
        car (str) 
    """

    cmp = 0
    for carac in mot:
        if carac == car :
            cmp += 1
    return cmp    


def min(lst):
    """trouve la valeur minimum d'une liste 

    Args:
        lst (list): 
    """
    if len(lst) == 0 :
        mini = None 

    else:    
        mini = lst[0]
        for i in range(1, len(lst)):
            if lst[i] < mini:
                mini = lst[i]

    return mini    

def etendue(lst):
    """calcule l'ecart entre le maximum et le minumuml d'une liste

    Args:
        lst (list): 

    Returns:
        (int): 
    """
    return max(lst) - min(lst)  

def sup_10(lst):
    """trouve le nombre de nombres supperieur à 10 dans la liste 

    Args:
        lst (lst): _

    Raises:
        ValueError: liste vide 

    Returns:
        _int: 
    """
    if len(lst) == 0 :
        raise ValueError('la liste est vide ')
    else:
        cmp = 0 
        for nb in lst:
            if nb > 10 :
                cmp += 1
        return cmp         


def somme_neg(lst):
    """calcule la valeur des nombres négatifs

    Args:
        lst (list): liste d'entier

    Raises:
        ValueError: c'est une liste vide 

    Returns:
        _int : somme des nombres négatifs
    """
    
    if len(lst) == 0 :
        raise ValueError("la liste est vide")
    else:
        cmp = 0
        for elt in lst:
            if elt < 0:
                cmp += elt 
        return cmp        



# dernière exercice 

def voy(car):
    if car in 'aeuioy':
        return True 
    else :
        return False


def syllabe(mot):
    con = False
    if voy(mot[0]):
           cmp = 1
    else:
        cmp = 0 
        con = True
    for i in range(1, len(mot)):
        if voy(mot[i]):
            if con :
                cmp += 1
                con = False
        else:
            con = True
    return cmp                                


def test_syllabe():
    assert (syllabe('tableau')) == 2
    assert (syllabe('beau')) == 1
    assert(syllabe('tatatatata')) == 5
    assert(syllabe('a')) == 1 

def test_somme_lst():
    assert(somme_lst([1, 2, 3, 4, 5])) == 15
    assert(somme_lst([0, 0, 0, 0, 0])) == 0
    assert(somme_lst([15, 42, 13, 24, 50])) == 144
    assert(somme_lst([1 ])) == 1
    
def test_max_lst():
    assert(max([1, 2, 3, 4, 5])) == 5
    assert(max([0, 0, 0, 0, 0])) == 0
    assert(max([15, 42, 13, 24, 50])) == 50
    assert(max([1])) == 1

def test_nb_occ():
    assert(nb_occ("tatata", 'a')) == 3   
    assert(nb_occ("tatata", 't')) == 3   
    assert(nb_occ("tttttttt", 'a')) == 0
    assert(nb_occ("aaaaaaa", 'a')) == 7

def test_min():
    assert(min([1, 2, 3, 4, 5])) ==  1  
    assert(min([0, 0, 0, 0, 0])) == 0
    assert(min([15, 42, 13, 24, 50])) == 13
    assert(min([1])) ==  1

def test_etendue():
    assert(etendue([1, 2, 3, 4, 5])) ==  4
    assert(etendue([0, 0, 0, 0, 0])) ==   0 
    assert(etendue([15, 42, 13, 24, 50])) == 37   
    assert(etendue([1])) ==      0

def test_supp_10():
    assert(sup_10([1, 2, 3, 4, 5])) ==  0    
    assert(sup_10([11, 11, 11 ])) ==  3   
    assert(sup_10([15, 42, 13, 24, 50])) == 5    
    assert(sup_10([10])) ==     0

def test_somme_neg():
    assert(somme_neg([0,0,0,0,0,0])) == 0
    assert(somme_neg([-2, -5, -4])) == -11
    assert(somme_neg([-5, 5, -9, 5])) == -14
    assert(somme_neg([15, 4, 2])) == 0
