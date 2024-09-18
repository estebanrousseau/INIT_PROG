#ex 5 
def somme_pair(lst):
    """fonction qui compte la somme des nombre pair dans la liste

    Args:
        lst (list): _description_liste de nombre reel

    return :
        somme des nombres pairs    
    """
    res = 0 

    for i in range(len(lst)):
        if lst[i] %2 == 0 :
            res += lst[i]
    return res        

def somme_n(n):
    """fait la somme des n premiers entiers

    Args:
        n (int): 

    return :
        somme des n premiers entiers    
    """
    res = 0
    for nb in range(n):
        res += n 
    return n     

def syracuse(n, val_ini):

    """calcule des termes de la suite de syracuse
        
    args : n (int)
           val_init (int)

    Returns:
        _type_: retourne le resultat de la suite de syracuse 
    """
    U = val_ini
    for i in range(n):
        if U %2 == 0 :
            U = U / 2
        else :
            U = U * 3  + 1    
    return U        


def test_syracuse():
    assert(syracuse(1, 6)) == 3
    assert(syracuse(2, 6)) == 10
    assert(syracuse(3, 6)) == 5
    assert(syracuse(0, 6)) == 6