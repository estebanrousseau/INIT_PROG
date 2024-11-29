def probleme_CV_PDF():
    car = input('entrez le texte: ')
    car_f = ''
    for i in range(0, len(car), 2):
        car_f += car[i]

    fonc = input('es-ce une fonction (o)(n): ')
    if fonc == 'o': 
        print('def', car_f + ':')
    else:
        print(car_f)    
    return car_f    

probleme_CV_PDF()

