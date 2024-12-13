#1.1
#  calcul de la moyenne des dépenses et difference pour chacun 
# 8 + 12 + 15 + 20 + 52 + 8 + 3 + 34 = 152 prix total 
# moyenne à payer pour chacun 118 / 5 = 30.4

#beatrice doit payer 30.4 - 8 = 22.4 euros
#pierre doit recevoir 7.6 euros
#marie doit recevoir 23.6 euros
#anna doit recevoir 21.6 euros
#sacha doit payer 30.4 euros

we_juin = {"béatrice" :{"pistache": 8},
           "pierre": {"pain": 12,
                      "film": 8, 
                      "pop-corn": 3,
                      "fromage": 15 }, 
            "marie": {"vin": 20,
                      "glace": 34},
            "anna": {"pizza": 52},
            'sacha': {}} 
            
#=====================================================
#1.3
#=====================================================
def somme_we(week):
    """renvoie la somme des dépenses pendant le week-end

    Args:
        week (dict): clé : nom , valeur : dict avec clé : article et valeur prix

    Returns:
        int: somme des depense
    """
    tot = 0 
    for article in week.values():
        tot += somme_personne(article)
    return tot        


def somme_personne(achat):
    """renvoie la somme des achats d'une unique personne

    Args:
        achat (dict): clé : article, valeur : prix

    Returns:
        int: prix total 
    """
    tot = 0 
    for prix in achat.values():
        tot += prix 
    return tot     

def moyenne_a_payer(week):
    """renvoie la moyenne à payer pour chacun 

    Args:
        week (dict): clé : nom , valeur : dict avec clé : article et valeur prix

    Returns:
        int: moyenne à payer
    """
    return somme_we(week) / len(week)



def remboussement(week):
    """affiche le bilan financier 

    Args:
        week (dict):  clé : nom , valeur : dict avec clé : article et valeur prix
    """
    moy = moyenne_a_payer(week)
    for personne, achat in week.items() :
        dette = somme_personne(achat) - moy
        if dette < 0 :
            print(personne, 'à', abs(dette), 'euros à verser aux autres')
        else:    
            print(personne, 'à', dette, 'euros à recevoir des autres')

remboussement(we_juin)            




#=====================================================
#exercice 2 
#=====================================================


def amour_reciproque(dico):
    lst_final = []
    for nom, amoureux in dico.items():
        if nom == dico[amoureux]:
            lst_final.append(nom)
    return lst_final