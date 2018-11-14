# Opiekun zwierzaka
# Wirtualny pupil

class Critter(object):
    """Wirtualny pupil"""
    #konstruktor
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    #metoda
    def __pass_time(self):
        self.hunger += 1
        self.boredom +=1


    #metoda wyswietlajaca informacje o obiekcie
    def __str__(self):
        stats = "Obiekt klasy Critter\n"
        stats += "name: " + self.name + "\nhunger:" + str(self.hunger) + "\nboredom:" + str(self.boredom) + "\n"
        return stats

    #własciwość mood
    @property
    def mood(self):
        unhappines = self.hunger + self.boredom
        if unhappines < 5:
            m = "szczesliwy"
        elif 5 <= unhappines <= 10:
            m = "zadowolony"
        elif 10 <= unhappines <=15:
            m = "podenerwowany"
        else:
            m = "wściekły"
        return m


    def talk(self):
        print("Nazywam sie",self.name, "i jestem teraz", self.mood, "\n")
        self.__pass_time()

    def eat(self):
        food = int(input("Jaka ilosc pożywienia chcesz dać zwierzakowi: "))
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self):
        fun = int(input("Ile minut chcesz bawić sie ze zwierzakiem: "))
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input("Jak chcesz nazwac swojego zwierzaka?: ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print(
            """Opiekun zwierzaka
            
            0 - zakończ
            1 - słuchaj zwierzaka
            2 - nakarm zwierzaka
            3 - pobaw sie ze zwierzakiem
            """
        )
        choice = input ("Co wybierasz?: ")
        if choice == "0":
            print("Do widzenia")
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            crit.eat()
        elif choice == "3":
            crit.play()
        elif choice == "4":
            print(crit)
        else:
            print("Nieprawidlowy wybór")

main()