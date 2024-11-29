"""Init Dev : TP9"""


# ==========================
# Petites bêtes
# ==========================

def toutes_les_familles(pokedex):
    """détermine l'ensemble des familles représentées dans le pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        set: l'ensemble des familles représentées dans le pokedex

    complexité lineaire O(N)
    """
    ensemble_fammille = set()
    for _, famille in pokedex:
        ensemble_fammille.add(famille)
    return ensemble_fammille     

def nombre_pokemons(pokedex, famille):
    """calcule le nombre de pokemons d'une certaine famille dans un pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)
        famille (str): le nom de la famille concernée

    Returns:
        int: le nombre de pokemons d'une certaine famille dans un pokedex
    complexite lineaire o(n)
    """
    nb_meme_famille = 0
    for _, type in pokedex:
        if famille == type :
            nb_meme_famille += 1
    return nb_meme_famille        

def frequences_famille(pokedex):
    """Construit le dictionnaire de fréqeunces des familles d'un pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str)
        et la valeur associée est le nombre de représentants de la famille (int)
    complexite lineaire
    """
    dico_freq = {}
    for _, famille in pokedex:
        if famille not in dico_freq:
            dico_freq[famille] = 1
        else:
            dico_freq[famille] += 1
    return dico_freq
        
def dico_par_famille(pokedex):
    """Construit un dictionnaire dont les les clés sont le nom de familles (str)
    et la valeur associée est l'ensemble (set) des noms des pokemons de cette
    famille dans le pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur associée est
        l'ensemble (set) des noms des pokemons de cette famille dans le pokedex

    complexite lineaire
    """
    dico_fam = {}
    for nom, famille in pokedex :
        if famille not in dico_fam :
            dico_fam[famille] = set()
            
        dico_fam[famille].add(nom)
        
    return dico_fam        

def famille_la_plus_representee(pokedex):
    """détermine le nom de la famille la plus représentée dans le pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        str: le nom de la famille la plus représentée dans le pokedex

        complexite lineaire
    """
    nom_max = None
    nb_max = None
    dico_freq = frequences_famille(pokedex)

    for famille in dico_freq:
        if nb_max is None or nb_max < dico_freq[famille]:
            nb_max = dico_freq[famille]
            nom_max = famille
    return nom_max        


# ==========================
# Petites bêtes (la suite)
# ==========================


def toutes_les_familles_v2(pokedex):
    """détermine l'ensemble des familles représentées dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        set: l'ensemble des familles représentées dans le pokedex
    """
    ens = set()
    for ens_type in pokedex.values():
        for type in ens_type:
            ens.add(type)
    return ens        

def nombre_pokemons_v2(pokedex, famille):
    """calcule le nombre de pokemons d'une certaine famille dans un pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)
        famille (str): le nom de la famille concernée

    Returns:
        int: le nombre de pokemons d'une certaine famille dans un pokedex
    """
    cmp = 0
    for ens_type in pokedex.values():
        if famille in ens_type:
            cmp += 1 
    return cmp        

def frequences_famille_v2(pokedex):
    """Construit le dictionnaire de fréqeunces des familles d'un pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur
        associée est le nombre de représentants de la famille (int)
    """
    dico_freq = {}
    for ens_type in pokedex.values():
        for type in ens_type:
            if type not in dico_freq :
                dico_freq[type] = 1
            else:
                dico_freq[type] += 1
    return dico_freq                

def dico_par_famille_v2(pokedex):
    """Construit un dictionnaire dont les les clés sont le nom de familles (str)
    et la valeur associée est l'ensemble (set) des noms des pokemons de
    cette famille dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur associée est
        l'ensemble (set) des noms des pokemons de cette famille dans le pokedex
    """
    dico_final = {}
    for poke, ens_type in pokedex.items():
        for type in ens_type:

            if type not in dico_final:
                dico_final[type] = set()
            dico_final[type].add(poke)  
    return dico_final          


def famille_la_plus_representee_v2(pokedex):
    """détermine le nom de la famille la plus représentée dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        str: le nom de la famille la plus représentée dans le pokedex
    """
    nom_max = None
    nb_max = None
    dico_freq = frequences_famille_v2(pokedex)

    for famille in dico_freq:
        if nb_max is None or nb_max < dico_freq[famille]:
            nb_max = dico_freq[famille]
            nom_max = famille
    return nom_max     

