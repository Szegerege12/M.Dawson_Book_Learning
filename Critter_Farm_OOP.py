"""
Farma zwierzaków
Kontrolowanie kilku zwierzaków na raz
Każdy zwierzak powinien mieć początkowo różne poziomy głodu lub nudy
"""
import random
class Critter(object):
    """Wirtualny pupil"""
    # konstruktor
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        stats = "Obiekt klasy Critter. Imie:"+ self.name +"głód:" + str(self.hunger) + "znudzenie:" +str(self.boredom)
        return stats

    # metoda nadajaca wartosci glodu i nudy
    def __pass_time(self):
        self.hunger -= 1
        self.hunger -= 1

     # właściwośc określająca stan zwierzaka(nastrój)
    @property
    def mood(self):
        happines = self.hunger + self.boredom
        if happines > 20:
            m = "szczęsliwy"
        elif 15 <= happines <= 20:
            m = "zadowolony"
        elif 10 <= happines <= 5:
            m = "obojetny"
        else:
            m = "zły"
        return m

    # metoda przedstawiająca się i mówiąca o nastroju
    def talk(self):
        print("Jestem",self.name, "i jestem teraz", self.mood, "\n")
        self.__pass_time()


    def eat(self):
        food = int(input("Jaka ilość pożywienia chcesz zaaplikować zwierzakom: "))
        self.hunger += food
        if self.hunger <= 10:
            self.hunger = 10
        self.__pass_time()


    def play(self):
        fun = int(input("Ile minut chcesz sie bawić ze zwierzakiem: "))
        self.boredom += fun
        if self.boredom <=10:
            self.boredom = 10
        self.__pass_time()


def main():

    #stado zwierzaków
    crit1 = Critter("Reksio",4,2)
    crit2 = Critter("Pluto",5,1)
    crit3 = Critter("Adrian",3,2)

    choice = None
    while choice != "0":
        print(
            """
            Farma zwierzaków
            MENU:
            
            0 - Zakońćż
            1 - Słuchaj zwierzaków
            2 - Nakarm zwierzaki
            3 - Baw sie ze zwierzakami
            4 - Wyświetl dane obiektów
            """)

        choice = input("Co wybierasz: ")
        if choice == "0":
            print("Zamykanie programu")
        elif choice == "1":
            crit1.talk()
            crit2.talk()
            crit3.talk()
        elif choice == "2":
            crit1.eat()
            crit2.eat()
            crit3.eat()
        elif choice == "3":
            crit1.play()
            crit2.play()
            crit3.play()
        elif choice == "4":
            print(crit1)
            print(crit2)
            print(crit3)

main()
