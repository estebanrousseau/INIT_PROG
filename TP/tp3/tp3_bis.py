from math import * 


def moy (lst):
    cmp = 0 
    res = 0 
    for elt in lst :
        cmp += 1
        res += elt

    return res/cmp 


def ecart_typt(lst):
    """_summary_

    Args:
        lst (_type_): _description_

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    if lst == []:
        raise ValueError("la liste est vide")
    else:
        moyenne = moy(lst)
        res = 0
        taille_lst = len(lst)
        for n in range(1, taille_lst):
            res += (1 / taille_lst) * (lst[n] - moyenne) ** 2
        return sqrt(res)

#print(ecart_typt([2, 4, 4, 4, 5, 5, 7, 9]))        


def annee_b(annee):
    """trouve si l'année est bisextille

    Args:
        annee (int): 

    Returns:
        bool: 
    """
    if annee % 400 == 0:
        res = True
    elif annee % 100 == 0:
        res = False
    elif annee % 4 == 0 :
        res = True
    else :
        res = False
    return res

def test_annee_b():
    assert(annee_b(2000))
    assert(annee_b(1900))
    assert(annee_b(2004))
    assert(annee_b(1500))



def trouve_annee_b(annee1, annee2):
    dep = annee1 + 1
    cmp = 0
    if annee2 - annee1 > 3 :
        while  not annee_b(dep) and dep < annee2 :
            dep += 1    

        for ann in range(dep , annee2   , 4 ):
            if annee_b(ann):
                cmp += 1 

    else :
        for ann in range(annee1 + 1 , annee2):
            if annee_b(ann):
                cmp += 1

    return cmp            
           
print(trouve_annee_b(1999, 2000))