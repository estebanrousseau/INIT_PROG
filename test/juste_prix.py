import random
     
def juste_prix():

    vrai_prix = random.randint(0, 1000)
    tentatives = 10
    while tentatives > 0 :
        
        prix_donne = int(input('entrez un nombre  '))
        if prix_donne == vrai_prix :
            print('Bravo vous avez gagné')
        
        elif prix_donne < vrai_prix :
            print('trop PETIT', 'il reste ', tentatives - 1, 'tentatives')

        else :
            print('trop GRAND ', 'il reste ', tentatives - 1, 'tentatives')  
        tentatives -= 1  

    if tentatives == 0 and prix_donne != vrai_prix :    
        print('Dommage vous avez perdu')        

juste_prix()