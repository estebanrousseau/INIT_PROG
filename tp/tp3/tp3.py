# exercice 1
def mystere_exo2(lst_nb):
    """compte les nombres pairs et impairs 

    Args:
        entree (list): [liste de nombres]

    Returns:
        bool : renvoie vrai si il y a plus de nombre impairs et faux dans le cas contraire
    """
    pair = 0
    impair = 0
    # pair(xxx) contient à chaque tour de boucle le nombre
    # nombre pair parcouru de la liste_nombres(entrée) 
    # pour impair(yyy) c'est les nombres impairs

    #  A COMPLETER
    for nombre in lst_nb:
        if nombre % 2 == 0:
            pair += 1
        else:
            impair += 1
    return pair >= impair


# exercice 2
def min_sup(liste_nombres, valeur):
    """trouve le plus petit nombre d'une liste supérieur à une certaine valeur

    Args:
        liste_nombres (list): la liste de nombres
        valeur (int ou float): la valeur limite du minimum recherché

    Returns:
        int ou float: le plus petit nombre de la liste supérieur à valeur
    """
    res = float('inf')
    # au début de chaque tour de boucle res est le plus petit élément
    # déjà énuméré supérieur à valeur

    for elem in liste_nombres:
        if valeur < elem < res:
            res = elem
    
    if res == float('inf'):
        res= None
    return res


def test_min_sup():
    assert min_sup([8, 12, 7, 3, 9, 2, 1, 4, 9], 5) == 7
    assert min_sup([-2, -5, 2, 9.8, -8.1, 7], 0) == 2
    assert min_sup([5, 7, 6, 5, 7, 3], 10) is None
    assert min_sup([], 5) is None


# exercice 3
def nb_mots(phrase):
    """Fonction qui compte le nombre de mots d'une phrase

    Args:
        phrase (str): une phrase dont les mots sont
        séparés par des espaces (éventuellement plusieurs)

    Returns:
        int: le nombre de mots de la phrase
    """    
    resultat = 0
    cp = ' '
    # au début de chaque tour de boucle
    # c1 vaut le caractère avant c2
    # c2 vaut chaque caractère parcouru successivement dans phrase
    # resultat vaut le nombre de mots trouver jusqu'à présent
    for c_act in phrase:
        if cp == ' ' and c_act != ' ':
            resultat = resultat + 1
        cp = c_act
    return resultat


def test_nb_mots():
    assert nb_mots("bonjour, il fait beau") == 4
    assert nb_mots("houla!     je    mets beaucoup   d'  espaces    ") == 6
    assert nb_mots(" ce  test ne  marche pas ") == 5
    assert nb_mots("") == 0  # celui ci non plus

mystere_exo2([1,4,6,-2,-5,3,10])

mystere_exo2([-4,5,-11,-56,5,-11])

def test_mystere_2():
    assert (mystere_exo2([2,3,4,5,6,8]))
    assert not (mystere_exo2([3,5,7]))
    assert(mystere_exo2([10,12,13,15]))
    assert not (mystere_exo2([3,5,7,8,10,13]))

print(nb_mots(" ce  test ne  marche pas "))



