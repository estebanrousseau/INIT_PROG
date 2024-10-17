import oiseaux
# --------------------------------------
# FONCTIONS
# --------------------------------------

#def test_recherche_oiseau():
 #   assert oiseaux.recherche_oiseau(...)==...

#def test_recherche_par_famille():
  #  assert oiseaux.recherche_par_famille(...)==...

def test_oiseau_le_plus_observe():
    assert oiseaux.oiseau_le_plus_observe(oiseaux.observations1)=="Moineau"
    assert oiseaux.oiseau_le_plus_observe(oiseaux.observations2)=="Rouge-gorge"
    assert oiseaux.oiseau_le_plus_observe(oiseaux.observations3)=="Mésange"
    assert oiseaux.oiseau_le_plus_observe([])==None

def test_oiseau_le_plus_observe_i():
    assert oiseaux.oiseau_le_plus_observe(oiseaux.observations1)=="Moineau"
    assert oiseaux.oiseau_le_plus_observe(oiseaux.observations2)=="Rouge-gorge"
    assert oiseaux.oiseau_le_plus_observe(oiseaux.observations3)=="Mésange"
    assert oiseaux.oiseau_le_plus_observe([])==None    


def test_caracteristique():
    assert oiseaux.caracteristique(oiseaux.oiseaux, 'Merle') == ("Merle", "Turtidé")
    assert oiseaux.caracteristique(oiseaux.oiseaux, 'Tourterelle') == ("Tourterelle", "Colombidé")
    assert oiseaux.caracteristique(oiseaux.oiseaux, 'Pie') == ("Pie", "Corvidé")
    assert oiseaux.caracteristique(oiseaux.oiseaux, 'Pic vert') == ("Pic vert", "Picidae")

def test_famille():
    assert oiseaux.meme_fammille(oiseaux.oiseaux, "Passereau") == ["Moineau", "Mésange", "Pinson", "Rouge-gorge"]
    assert oiseaux.meme_fammille(oiseaux.oiseaux, "Turtidé") == ["Merle"]
    assert oiseaux.meme_fammille(oiseaux.oiseaux, "Corvidé") == ["Pie"]
    assert oiseaux.meme_fammille([], "Corvidé") == []

def test_verif_obs():
    assert oiseaux.verif_observation(oiseaux.observations1) 
    assert oiseaux.verif_observation(oiseaux.observations1)
    assert not oiseaux.verif_observation([]) 
    assert not oiseaux.verif_observation([('woiso', 'j')]) 

def test_max_oiseaux():
    assert oiseaux.max_oiseaux(oiseaux.observations1) == 5
    assert oiseaux.max_oiseaux(oiseaux.observations2) == 5
    assert oiseaux.max_oiseaux(oiseaux.observations3) == 4
    assert oiseaux.max_oiseaux([]) is None

def test_moyenne_oiseau():
    assert oiseaux.moyenne_oiseau(oiseaux.observations1) == 3.0
    assert oiseaux.moyenne_oiseau(oiseaux.observations2) == 15 / 6
    assert oiseaux.moyenne_oiseau(oiseaux.observations3) == 16 / 6
    assert oiseaux.moyenne_oiseau([]) == 0

def test_compteur_meme_famille():
    assert oiseaux.compteur_meme_famille(oiseaux.oiseaux, [], "Passereau") == 0
    assert oiseaux.compteur_meme_famille([], oiseaux.observations1, "Passereau") == 0
    assert oiseaux.compteur_meme_famille([], [], "Passereau") == 0

    assert oiseaux.compteur_meme_famille(oiseaux.oiseaux, oiseaux.observations1, "Passereau") == 8
    assert oiseaux.compteur_meme_famille(oiseaux.oiseaux, oiseaux.observations1, "Turtidé") == 2
    assert oiseaux.compteur_meme_famille(oiseaux.oiseaux, oiseaux.observations1, "Colombidé") == 5

    assert oiseaux.compteur_meme_famille(oiseaux.oiseaux, oiseaux.observations2, "Picidae") == 0
    assert oiseaux.compteur_meme_famille(oiseaux.oiseaux, oiseaux.observations2, "Turtidé") == 2
    assert oiseaux.compteur_meme_famille(oiseaux.oiseaux, oiseaux.observations2, "Passereau") == 12


def test_cree_observation():
    assert oiseaux.cree_observation([], oiseaux.comptage1) == []
    assert oiseaux.cree_observation(oiseaux.oiseaux, []) == []
    assert oiseaux.cree_observation(oiseaux.oiseaux, oiseaux.comptage1 + [1]) == []

    print(oiseaux.cree_observation(oiseaux.oiseaux, oiseaux.comptage3))
    assert oiseaux.cree_observation(oiseaux.oiseaux, oiseaux.comptage1) == oiseaux.observations1
    assert oiseaux.cree_observation(oiseaux.oiseaux, oiseaux.comptage2) == oiseaux.observations2
    assert oiseaux.cree_observation(oiseaux.oiseaux, oiseaux.comptage3) == oiseaux.observations3
    

"""
def test_est_liste_observations():
    assert oiseaux.est_liste_observations(...)==...

def test_max_observations():
    assert oiseaux.max_observations(...)==...

def test_moyenne_oiseaux_observes():
    assert oiseaux.moyenne_oiseaux_observes(...)==...

def test_total_famille():
    assert oiseaux.total_famille(...)==...


def test_construire_liste_observations():
    assert oiseaux.construire_liste_observations(...)==...

def test_creer_ligne_sup():
    assert oiseaux.creer_ligne_sup(...)==...

def test_creer_ligne_noms_oiseaux():
    assert oiseaux.creer_ligne_noms_oiseaux(...)==...


"""
