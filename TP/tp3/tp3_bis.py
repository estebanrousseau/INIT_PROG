from math import * 


def moy (lst):
    cmp = 0 
    res = 0 
    for elt in lst :
        cmp += 1
        res += elt

    return res/cmp 


def ecart_typt(lst):
    if lst == []:
        raise ValueError("la liste est vide")
    else:
        moyenne = moy(lst)
        res = 0
        taille_lst = len(lst)
        for n in range(1, taille_lst):
            res += (1 / n) * (lst[n] - moyenne) ** 2
        return sqrt(res)

print(ecart_typt([2, 4, 4, 4, 5, 5, 7, 9]))        


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

def divisible_4(annee):
    return annee %4 == 0


def trouve_annee_b(annee1, annee2):
    dep = 0
    while divisible_4(annee1 + dep -1 ):
        dep = 1 
        annee_b1 += 1 
