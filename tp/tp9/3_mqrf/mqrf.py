
# ==========================
# La maison qui rend fou
# ==========================

def quel_guichet(mqrf, guichet):
    """Détermine le nom du guichet qui délivre le formulaire A-38

    Args:
        mqrf (dict): représente une maison qui rend fou
        guichet (str): le nom du guichet de départ qui est le nom d'un guichet de la mqrf

    Returns:
        str: le nom du guichet qui finit par donner le formulaire A-38
    """
    if guichet not in mqrf :
        return None
    else:
        trouve = False 
        i = 0
        guichet_act = guichet
        while not trouve and i < len(mqrf):
            if mqrf[guichet_act] is None:
                trouve = True

            else:
                i += 1 
                guichet_act = mqrf[guichet_act] 
        if i == len(mqrf):
            return None
        else:
            return guichet_act           

def quel_guichet_v2(mqrf, guichet):
    """Détermine le nom du guichet qui délivre le formulaire A-38
    ainsi que le nombre de guichets visités

    Args:
        mqrf (dict): représente une maison qui rend fou
        guichet (str): le nom du guichet de départ qui est le nom d'un guichet de la mqrf

    Returns:
        tuple: le nom du guichet qui finit par donner le formulaire A-38 et le nombre de
        guichets visités pour y parvenir
    """
    if guichet not in mqrf :
        return None
    else:
        trouve = False 
        i = 0
        guichet_act = guichet
        while not trouve and i < len(mqrf):
            if mqrf[guichet_act] is None:
                trouve = True

            else:
                i += 1 
                guichet_act = mqrf[guichet_act] 
        if i == len(mqrf):
            return None
        else:
            return (guichet_act, i + 1)


def quel_guichet_v3(mqrf, guichet):
    """Détermine le nom du guichet qui délivre le formulaire A-38
    ainsi que le nombre de guichets visités

    Args:
        mqrf (dict): représente une maison qui rend fou
        guichet (str): le nom du guichet de départ qui est le nom d'un guichet de la mqrf

    Returns:
        tuple: le nom du guichet qui finit par donner le formulaire A-38 et le nombre de
        guichets visités pour y parvenir
        S'il n'est pas possible d'obtenir le formulaire en partant du guichet de depart,
        cette fonction renvoie None
    """
    if guichet not in mqrf :
        return None
    else:
        trouve = False 
        i = 0
        guichet_act = guichet
        while not trouve and i < len(mqrf):
            if mqrf[guichet_act] is None:
                trouve = True

            else:
                i += 1 
                guichet_act = mqrf[guichet_act] 
        if i == len(mqrf):
            return None
        else:
            return (guichet_act, i + 1)

