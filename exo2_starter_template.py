from exo1_starter_template import Robot

class Robot():
    """ Robot class content here"""

class Human():   
    __sexe = ''
    def __init__(self, sexe=''):
        self.__sexe = sexe
        if sexe == 'Male' or sexe == 'Female':
            pass
        else:
            self.__sexe = 'Male'
        self.__sexe = sexe
        self.__nb_aliment = 0
    def manger(self, nb_aliment = 1):
        for i in range(nb_aliment):
            if self.__sexe == 'Male':
                print("nombre aliment mangé par l'homme : {}".format(i+1))
            else:
                print("nombre aliment mangé par la femme : {}".format(i+1))
            self.__nb_aliment

if __name__ == "__main__":
    my_Human = Human("Male")
    my_Human.manger(2)


# class Cyborg(Robot, Human):   

#     def __init__(self, name, sexe):   
#         Robot.__init__(self, name)
#         Human.__init__(self, sexe)



# cyborg = Cyborg('Deux Ex Machina', 'M')

# print(cyborg.name, 'sexe', cyborg.sexe)
# print('Charging battery...')
# cyborg.charge()
# cyborg.status()
# cyborg.eat('banana')
# cyborg.eat(['coca', 'chips'])
# cyborg.digest()

# cyborg.truc_fun()
            
