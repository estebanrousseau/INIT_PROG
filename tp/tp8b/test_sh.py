import super_hero as sh

avengers = {
'Spiderman': ( 5 , 5 , 'araignée aquatre pattes') ,
'Hulk': ( 7 , 4 , " Grand homme vert" ) ,
'Agent13': ( 2 , 3 , 'agent13') ,
'M Melin': ( 2 , 6 , 'expertenarchi') 
}

avengers2 = {
'Spiderman': ( 5 , 5 , 'araignée aquatre pattes') ,
'Hulk': ( 7 , 4 , " Grand homme vert" ) ,
'Agent13': ( 2 , 3 , 'agent13') ,
'M Melin': ( 2 , 6 , 'expertenarchi') ,
'chat gpt' : (0, 10, 'sauve la vie des etudiants')
}

def test_intel_moy():
    assert sh.intelligence_moyenne(avengers) == 18 // 4 
    assert sh.intelligence_moyenne({}) is None
    assert sh.intelligence_moyenne(avengers2) == 5

def test_plus_fort():
    assert sh.plus_fort(avengers) == 'Hulk'
    assert sh.plus_fort({}) is None
   

def test_cretin():
    assert sh.cretin(avengers) == 2
    assert sh.cretin({}) is None    

