def trouve(lst, cible):
    i = 0
    trouve = False
    while i < len(lst) and not trouve:
        if lst[i] == cible :
            trouve = True 
        else :
            i += 1 
    return False 

def cumul_seuil(dico, seuil):
    lst_val = list(dico.values()) 

    i = 0 
    trouve = False
    tot = 0 

    while i < len(lst_val) and not trouve :
        tot += lst_val[i]
        if tot == seuil :
            trouve = True 

        else :
            i += 1

    if i == len(lst_val):
        return tot       
    else :
        return None 

#-------------------------
#exercice 2 
#-------------------------


class Morticia :

    def __init__(self, lst_art, lst_prix):
        self.lst_art = lst_art
        self.lst_prix = lst_prix

    def morticia_add(self, art, prix):
        """ajoute un article dans une liste de course 

        Args:
            art (str): article à ajouter 
            prix (int): prix de l'article à ajouter
        """
        self.lst_art.append(art)
        self.lst_prix.append(prix)

    def morticia_sup(self, art):
        """supprime un article de la liste de course 

        Args:
            art (str): article à supprimer 

        """

        taille = len(self.lst_art)
        i = 0 
        trouve = False

        while i < taille and not trouve :
            
            if self.lst_art[i] == art :
                trouve = True
            else :
                i += 1 

        if trouve :
            self.lst_art.pop(i)
            self.lst_prix.pop(i)
               


    def morticia_modif_prix(self, art, new_prix):
        """modifie le prix d'un article 

        Args:
            art (str): article dont on souhaite modifier le prix
            new_prix (int): le nouveau prix 
        """

        taille = len(self.lst_art)
        i = 0 
        trouve = False

        while i < taille and not trouve :
            
            if self.lst_art[i] == art :
                trouve = True
            else :
                i += 1 

        if trouve :
            self.lst_prix[i] = new_prix

    
    def morticia_montant_total(self):
        """renvoie le prix total de la liste de course 

        Returns:
            int: total des courses
        """
        total = 0 
        for prix in self.lst_prix:
            total += prix
        return total   

    def morticia_article_plus_cher(self):
        """renvoie l'article le plus cher de la liste de course 

        Returns:
            str: article le plus cher 
        """
        art_max_prix = None 
        art_max = None 
        for i in range(len(self.lst_art)):

            prix = self.lst_prix[i]
            art = self.lst_art[i]

            if art_max_prix is None or prix >= art_max_prix :
                art_max_prix = prix
                art_max = art 
        return art_max        
    
    def __str__(self):
        """renvoie les atribut de l'objet 

        Returns:
            str: ne renvoie rien , la methode __str__ doit renvoyer un str pour ne pas crée une erreur
        """
        print(self.lst_art, self.lst_prix)
        return ""

#------------------------------------------------------------------------------------------------------------------------------------


class Gomez :

    def __init__(self, lst_course):
        self.lst_course = lst_course


    def gomez_add(self, art, prix):
        """ajoute un article dans une liste de course 

        Args:
            art (str): article à ajouter 
            prix (int): prix de l'article à ajouter
        """
        self.lst_course.append(art)
        self.lst_course.append(prix)

    def gomez_sup(self, art):
        """supprime un article de la liste de course 

        Args:
            art (str): article à supprimer 

        """

        taille = len(self.lst_course)
        i = 0 
        trouve = False

        while i < (taille - 1) and not trouve :
            
            if self.lst_course[i] == art :
                trouve = True
            else :
                i += 1 

        if trouve :
            self.lst_course.pop(i)
            self.lst_course.pop(i)
               


    def gomez_modif_prix(self, art, new_prix):
        """modifie le prix d'un article 

        Args:
            art (str): article dont on souhaite modifier le prix
            new_prix (int): le nouveau prix 
        """

        taille = len(self.lst_course)
        i = 0
        trouve = False

        while i < taille and not trouve :
            
            if self.lst_course[i] == art :
                trouve = True
            else :
                i += 2

        if trouve :
            self.lst_course[i + 1] = new_prix

    
    def gomez_montant_total(self):
        """renvoie le prix total de la liste de course 

        Returns:
            int: total des courses
        """
        total = 0 
        for i in range(1, len(self.lst_course), 2):
            total += self.lst_course[i]
        return total   

    def gomez_article_plus_cher(self):
        """renvoie l'article le plus cher de la liste de course 

        Returns:
            str: article le plus cher 
        """
        art_max_prix = None 
        art_max = None 
        for i in range(1, len(self.lst_course), 2):

            prix = self.lst_course[i]
            art = self.lst_course[i - 1]

            if art_max_prix is None or prix >= art_max_prix :
                art_max_prix = prix
                art_max = art 
        return art_max        
    
    def __str__(self):
        """renvoie les atribut de l'objet 

        Returns:
            str: ne renvoie rien , la methode __str__ doit renvoyer un str pour ne pas crée une erreur
        """
        print(self.lst_course)
        return ""
    

#---------------------------------------------------------------------------------------------------------------------------------------


class Mercredi :

    def __init__(self, lst_course):
        self.lst_course = lst_course


    def mercredi_add(self, art, prix):
        """ajoute un article dans une liste de course 

        Args:
            art (str): article à ajouter 
            prix (int): prix de l'article à ajouter
        """
        self.lst_course[art] = prix
        print("\nl'article", art, 'à été ajouté') 


    def mercredi_sup(self, art):
        """supprime un article de la liste de course 

        Args:
            art (str): article à supprimer 

        """
        if art in self.lst_course :
            self.lst_course.pop(art, None)
        else :
            print("\nL'ARTICLE", art, "N'EXISTE PAS, ENTREZ UN ARTICLE CORRECT")    
               


    def mercredi_modif_prix(self, art, new_prix):
        """modifie le prix d'un article 

        Args:
            art (str): article dont on souhaite modifier le prix
            new_prix (int): le nouveau prix 
        """
        if art in self.lst_course :
            self.lst_course[art] = new_prix 
            print("\nl'article", art, "coute maintenant", new_prix, 'euros')
        else:
            print("\nL'ARTICLE", art, "N'EXISTE PAS, ENTREZ UN ARTICLE CORRECT") 


    
    def mercredi_montant_total(self):
        """renvoie le prix total de la liste de course 

        Returns:
            int: total des courses
        """
        total = 0 
        for prix in self.lst_course.values():
            total += prix
        return total   

    def mercredi_article_plus_cher(self):
        """renvoie l'article le plus cher de la liste de course 

        Returns:
            str: article le plus cher 
        """


        art_max_prix = None 
        art_max = None 
        for art, prix in self.lst_course.items():

            if art_max_prix is None or prix >= art_max_prix :
                art_max_prix = prix
                art_max = art 
        return art_max        
    
    def __str__(self):
        """renvoie les atribut de l'objet 

        Returns:
            str: ne renvoie rien , la methode __str__ doit renvoyer un str pour ne pas crée une erreur
        """
        print(self.lst_course)
        return ""
    

#---------------------------------------------------------------------------------------------------------------------------------------


class Fetide :

    def __init__(self, lst_course):
        self.lst_course = lst_course


    def fetide_add(self, art, prix):
        """ajoute un article dans une liste de course 

        Args:
            art (str): article à ajouter 
            prix (int): prix de l'article à ajouter
        """
        self.lst_course.append((art, prix)) 


    def fetide_sup(self, art):
        """supprime un article de la liste de course 

        Args:
            art (str): article à supprimer 

        """

        taille = len(self.lst_course)
        i = 0 
        trouve = False

        while i < taille and not trouve :
            
            if self.lst_course[i][0] == art :
                trouve = True
            else :
                i += 1 

        if trouve :
            self.lst_course.pop(i)
               


    def fetide_modif_prix(self, art, new_prix):
        """modifie le prix d'un article 

        Args:
            art (str): article dont on souhaite modifier le prix
            new_prix (int): le nouveau prix 
        """

        taille = len(self.lst_course)
        i = 0 
        trouve = False

        while i < taille and not trouve :
            
            if self.lst_course[i][0] == art :
                trouve = True
            else :
                i += 1 

        if trouve :
            self.lst_course[i] = (self.lst_course[i][0], new_prix)

    
    def fetide_montant_total(self):
        """renvoie le prix total de la liste de course 

        Returns:
            int: total des courses
        """
        total = 0 
        for _, prix in self.lst_course:
            total += prix
        return total   

    def fetide_article_plus_cher(self):
        """renvoie l'article le plus cher de la liste de course 

        Returns:
            str: article le plus cher 
        """
        art_max_prix = None 
        art_max = None 
        for art, prix in self.lst_course:

            if art_max_prix is None or prix >= art_max_prix :
                art_max_prix = prix
                art_max = art 
        return art_max        
    
    def __str__(self):
        """renvoie les atribut de l'objet 

        Returns:
            str: ne renvoie rien , la methode __str__ doit renvoyer un str pour ne pas crée une erreur
        """
        print(self.lst_course)
        return ""    
    

def programme_principal()  :
    course = Mercredi({})
    running = True 
    while running :
        aff_question()
        question = input('entrez le numero de la question ou quittez (quit) ')

        if question == 'quit':
            running = False

        elif verif_int(question):
            repond_question(question, course)




def verif_int(car):
    return car >= '1' and car <= '6'
    


def aff_question():
    print('\n+--------------------+\n| MENU DES QUESTIONS |\n+--------------------+')    
    print('1: ajouter des article')  
    print('2: enlever de article') 
    print('3: modifier le prix de l\'article')   
    print('4: montant total des courses')
    print('5: article le plus cher')
    print('6: afficher la liste de course')
    

def repond_question(car, course):
    print("\n\n\n")

    if car == '1':
        art = input('entrez votre article ')
        prix = int(input('entrez le prix de l\'article '))
        course.mercredi_add(art, prix)

    elif car == '2':
        entre = input('entrez l\'article à enlever ') 
        course.mercredi_sup(entre)   

    elif car == '3':
        art = input('entrez l\'article dont vous souhaitez modifier le prix ')  
        prix = int(input('entrez le nouveau prix '))
        course.mercredi_modif_prix(art, prix)

    elif car == '4':
        print('Le prix total des courses est de:', course.mercredi_montant_total(), 'euros')  

    elif car == '5':
        print("L'article le plus cher est:", course.mercredi_article_plus_cher())      

    elif car == '6':
        print('voici la liste de course: ', course)    

        
    else :
        print('IL FAUT ENTREZ UNE COMLANDE CORRECT')

programme_principal()        