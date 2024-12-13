""" Fonctions utilitaires pour manipuler les matrices """

import API_matrice2 as m


def get_val_mat(matrice):
    """renvoie la liste plate des valeurs de la matrice 

    Args:
        matrice (tuple): une matrice 

    Returns:
        les valeur le la matrice: 
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
    return get_val_mat(matrice)[ligne * m.get_nb_colonnes(matrice) : ligne * m.get_nb_colonnes(matrice) + m.get_nb_colonnes(matrice)]


def get_colonnes(matrice, colonne):
    """revoie une colonne de la matrice

    Args:
        matrice (tuple): la matrice
        colonne (int): numero de la colonne

    Returns:
        list: liste d'une colonne
    """
    return [m.get_val(matrice, i, colonne) for i in range(m.get_nb_lignes(matrice))]


def get_diagonale_principale(matrice):
    """renvoie la diagonale pricipal de la matrice 

    Args:
        matrice (tuple): la matrice carré

    Returns:
        list: liste contenant la digonale pricipale de la matrice 
    """
    return [m.get_val(matrice, i, i) for i in range(m.get_nb_lignes(matrice))]



def get_diagonale_secondaire(matrice):
    """renvoie la diagonale secondaire de la matrice 

    Args:
        matrice (tuple): la matrice carré

    Returns:
        list: liste contenant la digonale secondaire de la matrice 
    """
    lst_final = []
    ligne = 0
    nb_col = m.get_nb_colonnes(matrice)

    for i in range(nb_col - 1, -1, -1):
        lst_final.append(m.get_val(matrice, ligne, i))
        ligne += 1
    return lst_final



def transpose(matrice_int):
    """transpose la matrice 

    Args:
        matrice_int (tuple): la matrice

    Returns:
        tuple: la transposé
    """
    mat = m.matrice(m.get_nb_colonnes(matrice_int), m.get_nb_lignes(matrice_int), 0)

    for i in range(m.get_nb_colonnes(matrice_int)):

        ligne = get_colonnes(matrice_int, i)
        for j in range(len(ligne)):
            m.set_val(mat, i, j, ligne[j])

    return mat


def is_triangulaire(mat):
    """trouve si la matrice est triangulaire 

    Args:
        mat (tuple): la matrice

    Returns:
        bool: vrai si triangulaire et faux sinon 
    """
    taille = m.get_nb_colonnes(mat)
    for ligne in range(taille):
        for colonne in range(ligne + 1, taille):
            if m.get_val(mat, ligne, colonne) != 0 :
                return False
    return True

def block(mat, ligne, colonne, hauteur, largeur):
    """renvoie le sous bloc commençant à une ligne et colonne donné et allant à une hauteur et largeur donné 

    Args:
        mat (tuple): la matrice
        ligne (int): ligne de depart
        colonne (int): colonne de depart 
        hauteur (int): hauteur de la sous matrice
        largeur (int): largeur de la matrice

    Returns:
        tuple: la sous matrice 
    """
    if ligne + hauteur  > m.get_nb_lignes(mat) or colonne + largeur > m.get_nb_colonnes(mat):
        return None
    
    else:
        mat_final = m.matrice(hauteur, largeur, 0)
        for lig in range(hauteur):
            for col in range(largeur):
                m.set_val(mat_final,lig, col, m.get_val(mat, ligne + lig, colonne + col))
        return mat_final        
    


def somme(mat1, mat2):

    if m.get_nb_colonnes(mat1) != m.get_nb_colonnes(mat2) or m.get_nb_lignes(mat1) != m.get_nb_lignes(mat2):
        print("les matrices n'ont pas le meme ordre, le calcul est donc impossible")

    else:    
        mat_final = m.matrice(m.get_nb_lignes(mat1), m.get_nb_colonnes(mat1), 0)

        for ligne in range(m.get_nb_lignes(mat1)):
            for colonne in range(m.get_nb_colonnes(mat2)):
                m.set_val(mat_final, ligne, colonne, m.get_val(mat1, ligne, colonne) + m.get_val(mat2, ligne, colonne))
        return mat_final        

