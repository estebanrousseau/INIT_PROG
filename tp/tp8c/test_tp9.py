import tp9 as t




def test_morticia():
    
    course_morticia = ['bave de crapeau', 'oeufs de dragon', 'lezards', 'ketchup', 'sel']
    facture = [17, 157, 17, 2, 1]


    morti = t.Morticia(course_morticia, facture)

    morti.morticia_add('pain', 2)
    assert morti.lst_art == ['bave de crapeau', 'oeufs de dragon', 'lezards', 'ketchup', 'sel', 'pain']
    assert morti.lst_prix == [17, 157, 17, 2, 1, 2]

    morti.morticia_sup('pain')
    assert morti.lst_art == ['bave de crapeau', 'oeufs de dragon', 'lezards', 'ketchup', 'sel']
    assert morti.lst_prix == [17, 157, 17, 2, 1]

    morti.morticia_modif_prix('sel', 200)
    assert morti.lst_art == ['bave de crapeau', 'oeufs de dragon', 'lezards', 'ketchup', 'sel']
    assert morti.lst_prix == [17, 157, 17, 2, 200]

    assert morti.morticia_montant_total() == 393

    assert morti.morticia_article_plus_cher() == 'sel'

    morti.morticia_sup('sel')
    assert morti.lst_art == ['bave de crapeau', 'oeufs de dragon', 'lezards', 'ketchup']
    assert morti.lst_prix == [17, 157, 17, 2]   

    assert morti.morticia_montant_total() == 193

    assert morti.morticia_article_plus_cher() == 'oeufs de dragon'



def test_gomez():

    course_gomez = [ "bave de crapeau" , 17 , "oeufs de dragon" , 157 ,"lézards" , 17 , "ketchup" , 2 , "sel" , 1]

    gom = t.Gomez(course_gomez)

    gom.gomez_add('pain', 2)
    assert gom.lst_course == ['bave de crapeau', 17, 'oeufs de dragon', 157, 'lézards', 17, 'ketchup', 2, 'sel', 1, 'pain', 2]

    gom.gomez_sup('pain')
    assert gom.lst_course == [ "bave de crapeau" , 17 , "oeufs de dragon" , 157 ,"lézards" , 17 , "ketchup" , 2 , "sel" , 1]

    gom.gomez_modif_prix('sel', 200)
    assert gom.lst_course == [ "bave de crapeau" , 17 , "oeufs de dragon" , 157 ,"lézards" , 17 , "ketchup" , 2 , "sel" , 200]

    assert gom.gomez_montant_total() == 393

    assert gom.gomez_article_plus_cher() == 'sel'

    gom.gomez_sup('sel')
    assert gom.lst_course == [ "bave de crapeau" , 17 , "oeufs de dragon" , 157 ,"lézards" , 17 , "ketchup" , 2]   

    assert gom.gomez_montant_total() == 193

    assert gom.gomez_article_plus_cher() == 'oeufs de dragon'    



def test_mercredi():

    course_mercredi = { "bave de crapeau" :17 , "oeufs de dragon" :157 , "lézards" :17 , "ketchup" :2 , "sel" :1}

    merc = t.Mercredi(course_mercredi)

    merc.mercredi_add('pain', 2)
    assert merc.lst_course == { "bave de crapeau" :17 , "oeufs de dragon" :157 , "lézards" :17 , "ketchup" :2 , "sel" :1, 'pain': 2}

    merc.mercredi_sup('pain')
    assert merc.lst_course == { "bave de crapeau" :17 , "oeufs de dragon" :157 , "lézards" :17 , "ketchup" :2 , "sel" :1}

    merc.mercredi_modif_prix('sel', 200)
    assert merc.lst_course == { "bave de crapeau" :17 , "oeufs de dragon" :157 , "lézards" :17 , "ketchup" :2 , "sel" :200}

    assert merc.mercredi_montant_total() == 393

    assert merc.mercredi_article_plus_cher() == 'sel'

    merc.mercredi_sup('sel')
    assert merc.lst_course == { "bave de crapeau" :17 , "oeufs de dragon" :157 , "lézards" :17 , "ketchup" :2}  

    assert merc.mercredi_montant_total() == 193

    assert merc.mercredi_article_plus_cher() == 'oeufs de dragon'    



def test_fetide():

    course_fetide = [( "bave de crapeau" , 17) , ( "oeufs de dragon" , 157) ,( "lézards" , 17) , ( "ketchup" , 2) , ( "sel" , 1) ]

    merc = t.Fetide(course_fetide)

    merc.fetide_add('pain', 2)
    assert merc.lst_course == [( "bave de crapeau" , 17) , ( "oeufs de dragon" , 157) ,( "lézards" , 17) , ( "ketchup" , 2) , ( "sel" , 1), ('pain', 2)]

    merc.fetide_sup('pain')
    assert merc.lst_course == [( "bave de crapeau" , 17) , ( "oeufs de dragon" , 157) ,( "lézards" , 17) , ( "ketchup" , 2) , ( "sel" , 1) ]

    merc.fetide_modif_prix('sel', 200)
    assert merc.lst_course == [( "bave de crapeau" , 17) , ( "oeufs de dragon" , 157) ,( "lézards" , 17) , ( "ketchup" , 2) , ( "sel" , 200) ]

    assert merc.fetide_montant_total() == 393

    assert merc.fetide_article_plus_cher() == 'sel'

    merc.fetide_sup('sel')
    assert merc.lst_course == [( "bave de crapeau" , 17) , ( "oeufs de dragon" , 157) ,( "lézards" , 17) , ( "ketchup" , 2) ]

    assert merc.fetide_montant_total() == 193

    assert merc.fetide_article_plus_cher() == 'oeufs de dragon'   