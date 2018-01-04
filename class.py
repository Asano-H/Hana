

class Dog:
    def __init__(self,init_power,max_power):
        self.__init_power = init_power
        self.__max_power = max_power
        self.__now_power = 5

    def bork(self):
        print("WanWan")
        print("now_power= ",self.__now_power)
        print("init_power= ",self.__init_power)
        print("max_power= ",self.__max_power)

    def eat(self,food):
        return "unti"

    def sleep(self,times):
        sleep_time = times * 4
        if self.__now_power >= self.__max_power:
            pass

        else:
        	for i in range(sleep_time):
        		self.__now_power += 3

        power = self.__now_power

        if self.__now_power >= self.__max_power:
            self.__now_power = self.__max_power
            power = self.__now_power

        return power
    

if __name__=="__main__":

	siba_dog = Dog(1,7)
	dobel = Dog(110,1000)

	siba_dog.bork()
	siba_dog.now_power = 10
	siba_dog.bork()
	siba_unti = siba_dog.eat("meat")
	print(siba_unti)


	dobel.bork()
	dobel_unti = dobel.eat("meat")
	print(dobel_unti)
	now_power = dobel.sleep(600)
	print(now_power)

	dobel.bork()