""" Fonctions utilitaires pour manipuler les matrices """

import API_matrice as m


def get_val_mat(matrice):
    """renvoie la liste plate des valeurs de la matrice 

    Args:
        matrice (tuple): une matrice 

    Returns:
        : 
    """
    return [m.get_val(matrice, i, j) for i in range(m.get_nb_lignes(matrice)) for j in range(m.get_nb_colonnes(matrice))]

def get_ligne(matrice,ligne):
    """renvoie un ligne d'une matrice 

    Args:
        matrice (tuple): la matrice 
        ligne (int): numero d'une ligne 

    Returns:
        list: la ligne concerné
    """
    return [m.get_val(matrice, i, j) for i in range(m.get_nb_lignes(matrice)) for j in range(m.get_nb_colonnes(matrice))][ligne * m.get_nb_colonnes(matrice) : ligne * m.get_nb_colonnes(matrice) + m.get_nb_colonnes(matrice)]


def get_colonnes(matrice, colonne):
    """revoie une colonne de la matrice

    Args:
        matrice (tuple): la matrice
        colonne (int): numero de la colonne

    Returns:
        list: liste d'une colonne
    """
    return [matrice[2][i + colonne] for i in range(0, len(matrice[2]))]


def get_diagonale_principale(matrice):
    """renvoie la diagonale pricipal de la matrice 

    Args:
        matrice (tuple): la matrice carré

    Returns:
        list: liste contenant la digonale pricipale de la matrice 
    """
    return [get_val(matrice, i, i) for i in range(get_nb_lignes(matrice))]



def get_diagonale_secondaire(matrice):
    """renvoie la diagonale secondaire de la matrice 

    Args:
        matrice (tuple): la matrice carré

    Returns:
        list: liste contenant la digonale secondaire de la matrice 
    """
    lst_final = []
    ligne = 0
    nb_col = get_nb_colonnes(matrice)

    for i in range(nb_col - 1, -1, -1):
        lst_final.append(get_val(matrice, ligne, i))
        ligne += 1
    return lst_final



def transpose(matrice_int):
    mat = matrice(get_nb_colonnes(matrice_int), get_nb_lignes(matrice_int), 0)

    for i in range(get_nb_colonnes(matrice_int)):

        ligne = get_colonnes(matrice_int, i)
        for j in range(len(ligne)):
            set_val(mat, i, j, ligne[j])

    return mat



mat1 = (3, 4, [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])



m.affiche(mat1)
#print(transpose(mat1))