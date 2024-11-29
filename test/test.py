dico = 'art prix'
dico = list(dico)
#print(dico)
a = '1,2,3'
#print(a.split(','))

a = {'a','b'}
b = {'c', 'd'}

#print(a.add(b))



#------------------------------------------
dico = {1: 1, 2: 2, 3: 3, 4: 4}

def exemple1(dico):

    for val in dico.values():
        print(val)



def exmple2(dico):

    for cle in dico:
        print( dico[cle] )

exemple1(dico)
exmple2(dico)