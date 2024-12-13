"""
Init Dev : TP10
Exercice 2 : Ecosystème
"""

def extinction_immediate(ecosysteme, animal):
    """
    renvoie True si animal s'éteint immédiatement dans l'écosystème faute
    de nourriture
    """
    return not ecosysteme[animal] in ecosysteme


def en_voie_disparition(ecosysteme, animal):
    """
    renvoie True si animal s'éteint est voué à disparaitre à long terme
    """
    trouve = False
    i = 0
    espece = animal 
    while not trouve and i < len(ecosysteme):

        if espece not in ecosysteme :
            trouve = True 

        elif espece is None:  # A REVOIR 
            return False      #

        else:
            i += 1
            espece = ecosysteme[espece]
    return trouve           


def animaux_en_danger(ecosysteme):
    """ renvoie l'ensemble des animaux qui sont en danger d'extinction immédiate"""
    ens_ext = set()
    for animal in ecosysteme:
        if extinction_immediate(ecosysteme, animal):
            ens_ext.add(animal)
    return ens_ext


def especes_en_voie_disparition(ecosysteme):
    """ renvoie l'ensemble des animaux qui sont en voués à disparaitre à long terme
    """
    ens_disp = set()
    for animal in ecosysteme:
        if en_voie_disparition(ecosysteme, animal):
            ens_disp.add(animal)
    return ens_disp




