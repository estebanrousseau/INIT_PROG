def mdp():
    
    nb = int(input("entrer un nombre "))

    if nb < 0 and nb > 10000000 :
        raise ValueError('uhhufh')
    else:
        
        for i in range(10000001):
            #print(i)
            if i == nb:
                print("le mot de passe est " , nb )
