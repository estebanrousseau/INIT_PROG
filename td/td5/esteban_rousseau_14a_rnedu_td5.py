def point_obtenu(resultat, bareme):
    somme = 0 
    for i in range(2, len(resultat)):
        somme += bareme[resultat[i]]