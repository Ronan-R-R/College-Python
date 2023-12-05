class animal():
    def __init__(self,an):
        self.animalName = an

    @property
    def animalName(self):
        return self.__animalName
    
    @animalName.setter
    def animalName(self, an):
        self.__animalName = an
    def whatIsOnTheMenu(self):
        return "Hmm, " + str(self.animalName) + " must eat the usual stuff. \n"
    
class Dog(animal):
    def __init__(self, an, tf):
        super().__init__(an)
        self.todaysfood = tf

    @property
    def todaysfood(self):
        return self.__todaysfood
    
    @todaysfood.setter
    def todaysfood(self, fc):
        self.__todaysfood = fc

    def whatIsOnTheMenu(self):
        if(self.todaysfood == ""):
            return super().whatIsOnTheMenu()
        else:
            return "Today, " + str(self.animalName) + " is eating " + str(self.todaysfood) + ". \n"
        
myDog = Dog("Bonnie", "Salads")
print(myDog.whatIsOnTheMenu())
myDog.todaysfood = ""
print(myDog.whatIsOnTheMenu())

myDog.animalName = "Sally"
myDog.todaysfood = "a treat"
print("******************************************************")
print(myDog.whatIsOnTheMenu())