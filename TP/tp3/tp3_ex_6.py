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

    