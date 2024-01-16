from exo1_starter_template import Robot
from time import sleep

# * Réutiliser la class Robot faite dans l'exo 1. *Sans copier/coller dans le fichier ;)*
# * Un humain doit posséder un sexe attribuable à sa création
# * Un humain doit pouvoir manger un ou plusieurs aliments
# * Un humain doit pouvoir digérer ce qu'il a mangé *pas très important, faire en dernier si vous avez le temps*
# * Un Cyborg doit être une combinaison d'un humain et d'un robot
# * Bonus : ajouter une méthode fun au Cyborg

class Human():   
    __sexe = ''
    def __init__(self, sexe=''):
        if sexe == 'Male' or sexe == 'Female':
            self.__sexe = sexe
        else:
            self.__sexe = 'Male'
        self.__nb_aliment = 0
        self.__food_eat = []
        
    def H_eat(self, food):
        if type(food) is str:
            self.__nb_aliment += 1
            if self.__sexe == 'Male':
                print("food eat by the man : {}".format(food))
            else:
                print("food eat by the woman : {}".format(food))
            self.__food_eat.append(food)
        else:
            for i in food:
                if self.__sexe == 'Male':
                    print("food eat by the man : {}".format(i))
                else:
                    print("food eat by the woman : {}".format(i))
                self.__nb_aliment += 1
                self.__food_eat.append(i)
        
    def H_digest(self):
        d = ""
        for i in range(self.__nb_aliment):
            print("Aliment digéré : {}/{}".format(i+1, self.__nb_aliment), end='\r', flush=True)
            del self.__food_eat[0]
            sleep(1)
        print()
        print("J'ai fini de digérer !")

    @property
    def food_eat(self):
        return self.__food_eat
    @property
    def sexe(self):
        return self.__sexe

class Cyborg(Robot, Human):   
    def __init__(self, name, sexe):   
        Robot.__init__(self, name)
        Human.__init__(self, sexe)

if __name__ == "__main__":
    my_Human = Human("Female")
    my_Human.H_eat('Tomato')
    my_Human.H_eat(['Water', 'Fish'])
    print(my_Human.food_eat)
    my_Human.H_digest()
    print(my_Human.food_eat)


    cyborg = Cyborg('Scooby-Doo 2', 'Male')

    print(cyborg.name, 'sexe', cyborg.sexe)
    print('Charging battery...')
    cyborg.battery_charge()
    cyborg.get_etat()
    cyborg.H_eat('banana')
    cyborg.H_eat(['coca', 'chips'])
    cyborg.H_digest()

# cyborg.truc_fun()
