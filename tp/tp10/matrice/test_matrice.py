""" tests pour les API matrices
    Remarques : tous les tests de ce fichier doivent passer
    quelle que soit l'API utilisée
"""
import API_matrice2 as API
import utilitaire_matrice as u

def matrice1():
    """ définition d'une matrice pour les tests """
    mat1 = API.matrice(3, 4, None)
    API.set_val(mat1, 0, 0, 10)
    API.set_val(mat1, 0, 1, 11)
    API.set_val(mat1, 0, 2, 12)
    API.set_val(mat1, 0, 3, 13)
    API.set_val(mat1, 1, 0, 14)
    API.set_val(mat1, 1, 1, 15)
    API.set_val(mat1, 1, 2, 16)
    API.set_val(mat1, 1, 3, 17)
    API.set_val(mat1, 2, 0, 18)
    API.set_val(mat1, 2, 1, 19)
    API.set_val(mat1, 2, 2, 20)
    API.set_val(mat1, 2, 3, 21)
    return mat1



def matrice2():
    mat2 = API.matrice(2, 3, None)
    API.set_val(mat2, 0, 0, 'A')
    API.set_val(mat2, 0, 1, 'B')
    API.set_val(mat2, 0, 2, 'C')
    API.set_val(mat2, 1, 0, 'D')
    API.set_val(mat2, 1, 1, 'E')
    API.set_val(mat2, 1, 2, 'F')
    return mat2

def matrice3():

    mat3 = API.matrice(3, 3, None)
    API.set_val(mat3, 0, 0, 2)
    API.set_val(mat3, 0, 1, 7)
    API.set_val(mat3, 0, 2, 6)
    API.set_val(mat3, 1, 0, 9)
    API.set_val(mat3, 1, 1, 5)
    API.set_val(mat3, 1, 2, 1)
    API.set_val(mat3, 2, 0, 4)
    API.set_val(mat3, 2, 1, 3)
    API.set_val(mat3, 2, 2, 8)
    return mat3

def test_get_nb_lignes():

    matrice_1 = matrice1()
    matrice_2 = matrice2()
    matrice_3 = matrice3()
    assert API.get_nb_lignes(matrice_1) == 3
    assert API.get_nb_lignes(matrice_2) == 2
    assert API.get_nb_lignes(matrice_3) == 3

def test_get_nb_colonnes():

    mat_1 = matrice1()
    mat_2 = matrice2()
    mat_3 = matrice3()
    assert API.get_nb_colonnes(mat_1) == 4
    assert API.get_nb_colonnes(mat_2) == 3
    assert API.get_nb_colonnes(mat_3) == 3

def test_get_val():

    matr1 = matrice1()
   
    matr2 = matrice2()

    matr3 = matrice3()

    assert API.get_val(matr1, 0, 1) == 11
    assert API.get_val(matr1, 2, 1) == 19
    assert API.get_val(matr2, 1, 1) == 'E'
    assert API.get_val(matr2, 0, 2) == 'C'
    assert API.get_val(matr3, 2, 0) == 4
    assert API.get_val(matr3, 1, 0) == 9
"""
def test_sauve_charge_matrice():
     #

    la_matrice = matrice2()
    API.sauve_matrice(la_matrice, "matrice.csv")
    
    matrice_bis = API.charge_matrice_str("matrice.csv")
    assert la_matrice == matrice_bis

"""

def test_get_ligne():
    mat = matrice1()
    assert u.get_ligne(mat, 0) == [10, 11, 12, 13]
    assert u.get_ligne(mat, 1) == [14, 15, 16, 17]
    assert u.get_ligne(mat, 2) == [18, 19, 20, 21]

def test_get_colonne():
    mat = matrice1()
    assert u.get_colonnes(mat, 0) == [10, 14, 18]  
    assert u.get_colonnes(mat, 1) == [11, 15, 19]    
    assert u.get_colonnes(mat, 2) == [12, 16, 20]    
    assert u.get_colonnes(mat, 3) == [13, 17, 21]   

def test_get_diago():
    mat = matrice3()
    assert u.get_diagonale_principale(mat)  == [2, 5, 8]

    assert u.get_diagonale_secondaire(mat) == [6, 5, 4]

def test_transpose():
    mat1 = matrice1()
    mat2 = matrice2()
    mat3 = matrice3()

    assert u.transpose(mat1) == [[10, 14, 18], [11, 15, 19], [12, 16, 20], [13, 17, 21]]
    assert u.transpose(mat2) == [['A', 'D'],['B', 'E'], ['C', 'F']]
    assert u.transpose(mat3) == [[2, 9, 4], [7, 5, 3], [6, 1 ,8]]

def test_is_triangulaire():
    mat1_tri = [[1, 0, 0], [2, 3, 0], [3, 4, 5]]
    mat2_tri = [[1, 0, 0, 0], [2, 3, 0, 0], [3, 4, 5, 0], [5, 5, 5, 5]]
    mat3_pas_tri = [[1, 0, 0], [2, 3, 1], [3, 4, 5]]
    mat4_pas_tri = [[1, 0, 0, 4], [2, 3, 0, 0], [3, 4, 5, 0], [5, 5, 5, 5]]

    assert u.is_triangulaire(mat1_tri)
    assert u.is_triangulaire(mat2_tri)
    assert not u.is_triangulaire(mat3_pas_tri)
    assert not u.is_triangulaire(mat4_pas_tri)

def test_block():
    mat1 = matrice1()
    
    assert u.block(mat1, 1, 1, 2, 3) == [[15, 16, 17], [19, 20, 21]]
    assert u.block(mat1, 0, 1, 3, 3) == [[11, 12, 13], [15, 16, 17], [19, 20, 21]]
    assert u.block(mat1, 0, 1, 0, 3) == []
    assert u.block(mat1, 0, 0, 3, 4) == matrice1()
    assert u.block(mat1, 2, 3, 1, 1) == [[21]]
    assert u.block(mat1, 0, 3, 3, 1) == [[13], [17], [21]]

    assert u.block(mat1, 5, 5, 1, 1) is None
    assert u.block(mat1, 2, 5, 1, 1) is None
    assert u.block(mat1, 1, 1, 18, 1) is None
    assert u.block(mat1, 2, 2, 1, 19) is None


def matrice4():
    mat4 = API.matrice(3, 3, None)
    API.set_val(mat4, 0, 0, 1)
    API.set_val(mat4, 0, 1, 2)
    API.set_val(mat4, 0, 2, 3)
    API.set_val(mat4, 1, 0, 4)
    API.set_val(mat4, 1, 1, 5)
    API.set_val(mat4, 1, 2, 6)
    API.set_val(mat4, 2, 0, 7)
    API.set_val(mat4, 2, 1, 8)
    API.set_val(mat4, 2, 2, 9)    


def test_somme():
    mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

    assert u.somme(mat1, mat2) == [[10, 10, 10], [10, 10, 10], [10, 10, 10]]
