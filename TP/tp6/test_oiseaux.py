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
    assert oiseaux.oiseau_le_plus_observe(oiseaux.observations2)=="Tourterelle"
    assert oiseaux.oiseau_le_plus_observe(oiseaux.observations3)=="Mésange"
    assert oiseaux.oiseau_le_plus_observe([])==None

def test_oiseau_le_plus_observe_i():
    assert oiseaux.oiseau_le_plus_observe(oiseaux.observations1)=="Moineau"
    assert oiseaux.oiseau_le_plus_observe(oiseaux.observations2)=="Tourterelle"
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
