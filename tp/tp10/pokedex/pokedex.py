"""Init Dev : TP10"""

# =====================================================================
# Exercice 1 : Choix de modélisation et complexité
# =====================================================================
# Modélisation n°1
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v1 dans le fichier de tests

def appartient_v1(pokemon, pokedex): 
    """ renvoie True si pokemon (str) est présent dans le pokedex 
        complexité: O(N)
        invariant: le pokemon n'a pas été trouvé jusqu'a i itération 
    """
    for poke, _ in pokedex:
        if poke == pokemon:
            return True
    return False    


def toutes_les_attaques_v1(pokemon, pokedex): 
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    complexité: O(N)
    invariant: ens_type contient l'ensenble des type du pokemon pour chaque tour de boucle 
    """
    ens_type = set()
    for poke, type in pokedex :
        if poke == pokemon:
            ens_type.add(type)
    return ens_type


def nombre_de_v1(attaque, pokedex): 
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    complexité: O(N)
    invariant: cmp contient le nombres de pokemon ayant le type recherché pour chaque tour de boucle 
    """
    cmp = 0
    for _, type in pokedex:    
        if type == attaque :
            cmp += 1
    return cmp        



def attaque_preferee_v1(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    complexité: O(N)
    invariant: maxi_type  contient le type ayant le plus d'occurence dans le pokedex 
               maxi_occ  contient le le nombre d'occurences du type ayant le plus d'occurence dans le pokedex  
    """
    dico_freq = {}
    maxi_occ = None
    maxi_type = None

    for _, type in pokedex:

        if type not in dico_freq:
            dico_freq[type] = 1
        else :
            dico_freq[type] += 1

        if maxi_occ is None or dico_freq[type] > maxi_occ:
            maxi_occ = dico_freq[type]
            maxi_type = type 
            
    return maxi_type   


# =====================================================================
# Modélisation n°2
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v2 dans le fichier de tests

def appartient_v2(pokemon, pokedex):
    """ renvoie True si pokemon (str) est présent dans le pokedex 
        complexité O(1)
        """
    return pokemon in pokedex


def toutes_les_attaques_v2(pokemon, pokedex):
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    complexité O(1)
    """
    if appartient_v2(pokemon, pokedex):
        return pokedex[pokemon]


def nombre_de_v2(attaque, pokedex):
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    complexité O(N)
    invariant: cmp contient le nombres de pokemon ayant le type recherché pour chaque tour de boucle 
    """
    cmp = 0
    for ens_type in pokedex.values() :
        if attaque in ens_type :
            cmp +=1 
    return cmp         


def attaque_preferee_v2(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    complexité: O(N)
    invariant: maxi_type  contient le type ayant le plus d'occurence dans le pokedex 
               maxi_occ  contient le le nombre d'occurences du type ayant le plus d'occurence dans le pokedex  
    """
    dico_freq = {}
    maxi_occ = None
    maxi_type = None

    for ens_type in pokedex.values():
        for type in ens_type:

            if type not in dico_freq:
                dico_freq[type] = 1
            else :
                dico_freq[type] += 1

            if maxi_occ is None or dico_freq[type] > maxi_occ:
                maxi_occ = dico_freq[type]
                maxi_type = type 
            
    return maxi_type  

# =====================================================================
# Modélisation n°3
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v3 dans le fichier de tests


def appartient_v3(pokemon, pokedex):
    """ renvoie True si pokemon (str) est présent dans le pokedex
        complexité O(N)
        invariant: le pokemon n'a pas été trouvé jusqu'a i itération  
    """
    for ens_poke in pokedex.values():
        if pokemon in ens_poke:
            return True
    return False    


def toutes_les_attaques_v3(pokemon, pokedex):
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    complexité O(N)
    invariant: ens_type contient tous les types du pokemon recherché trouvé à chaque tour de boucle
    """
    ens_type = set()
    for type_, ens_poke in pokedex.items() :
        if pokemon in ens_poke :
            ens_type.add(type_)
    return ens_type        


def nombre_de_v3(attaque, pokedex):
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    complexité O(1)
    """
    if attaque in pokedex:
        return len(pokedex[attaque])
    else:
        return 0


def attaque_preferee_v3(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    complexité O(N)
    maxi_type  contient le type ayant le plus d'occurence dans le pokedex 
    maxi_occ  contient le le nombre d'occurences du type ayant le plus d'occurence dans le pokedex 
    """
    maxi_occ = None
    maxi_type = None
    for type, ens_poke in pokedex.items() :
        if maxi_occ is None or len(ens_poke) > maxi_occ :
            maxi_occ = len(ens_poke)
            maxi_type = type 
    return maxi_type        




#+============================================================+
#|complexité |appartient|les attaques|nombres_de| attaque_pref|
#|===========|==========|============|==========|=============|
#|version n°1|    N     |     N      |    N     |      N      |
#|===========|==========|============|==========|=============|
#|version n°2|    1     |     1      |    N     |      N      |
#|===========|==========|============|==========|=============|
#|version n°3|    N     |     N      |    1     |      N      |
#+============================================================+




# =====================================================================
# Transformations
# =====================================================================

# Version 1 ==> Version 2

def v1_to_v2(pokedex_v1):
    """
    param: prend en paramètre un pokedex version 1
    renvoie le même pokedex mais en version 2
    """
    dico_v2 = {}
    for poke, type in pokedex_v1 :
        if poke not in dico_v2 :
            dico_v2[poke] = set()
        dico_v2[poke].add(type)  
    return dico_v2      


# Version 1 ==> Version 2

def v2_to_v3(pokedex_v2):
    """
    param: prend en paramètre un pokedex version2
    renvoie le même pokedex mais en version3
    """
    dico_v3 = {}
    for poke, ens_type in pokedex_v2.items():
        for type in ens_type:
            if type not in dico_v3:
                dico_v3[type] = set()
            dico_v3[type].add(poke)
    return dico_v3            

