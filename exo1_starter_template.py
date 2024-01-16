from time import sleep

class Robot():
        
    """
      Give your best code here ( •̀ ω •́ )✧
    """

    def __init__(self, name='', power=False):
        self.__power = False
        self.__current_speed = 0
        self.__battery_level = 0
        self.__states = ['shutown', 'running']
        self.__name = name


    def power_on(self):
        self.__power = True
    def power_off(self):
        self.__power = False

    def battery_charge(self):
        progression = ''
        while self.__battery_level < 100:
            self.__battery_level += 1
            if self.__battery_level < 100:
                progression += '-'
            else:
                progression += '>'
            sleep(0.05)
            print("niveau de battery : {:100s} ({})%".format(progression, self.__battery_level), end='\r', flush = True)
        print("")


    @property
    def get_vitesse(self):
        return self.__current_speed
    @property
    def name(self):
        return self.__name

    def get_etat(self):
        print("Nom robot : {}".format(self.__name))
        print("allumé ou éteint : {}".format(self.__power))
        print("niveau de battery : {}%".format(self.__battery_level))
        print("vitesse de déplacement : {}".format(self.__current_speed))

        if self.__power == False:
            print("état du robot : {}".format(self.__states[0]))
        else:
            print("état du robot : {}".format(self.__states[1]))

    def stop_vitesse(self):
        self.__current_speed = 0

if __name__ == "__main__":
    my_robot = Robot("Scooby-doo")
    my_robot.battery_charge()
    my_robot.power_on()
    my_robot.get_etat()
