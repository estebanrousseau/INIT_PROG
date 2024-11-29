#----------------------------------------------------------------------------------------------------------------------
# exercice 2 
#----------------------------------------------------------------------------------------------------------------------




#ligne 1 
# description de spiderman avenger['spiderman'][2]
# avanger['gamora'][1]
# avanger['agent 13']

def intelligence_moyenne(dico):
    """trouve la moyenne de l'inteligence des membre des avengers

    Args:
        dico (dict): dico d'avenger

    Returns:
        int : moyenne de l'inteligence 
    """
    if len(dico) == 0:
        return None 
    else :
        
        intel_tot = 0
        for val in dico.values():
            intel_tot += val[1]
        return intel_tot // len(dico)    
    

def plus_fort(dico):
    """renvoie le personnage le plus fort 

    Args:
        dico (dict): dico des avengers

    Returns:
        str: personnage le plus fort
    """
    if len(dico) == 0:
        return None
    
    else:
        f_max = 0
        p_max = ''
        for cle, val in dico.items():
            if val[0] > f_max : 
                f_max = val[0]
                p_max = cle

        return p_max  


def cretin(dico):
    """renvoie le nombre d cretion dans la team 

    Args:
        dico (dict): dico des avengers

    Returns:
        int : nombre de cretins 
    """
    if len(dico) == 0 :
        return None

    else :
        moy = intelligence_moyenne(dico)    
        cpt = 0
        for hero, val in dico.items():
            if val[1] > moy :
                cpt += 1
        return cpt            