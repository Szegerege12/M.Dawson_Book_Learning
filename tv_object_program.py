# Program symulujący telewizor
# użytkownik powinien mieć możliwość wprowadzenia nr kanału
# powinien mieć możliwosć zmiany głośności
# zadbaj o zakresy kanałów i głośności

class Televison(object):
    """Wirtualny telewizor"""
    #konstruktor pozwala na okreslenie poczatkowych atrybutów obiektu
    def __init__(self, canal = 1, volume = 1):
        self.canal = canal
        self.volume = volume

    # metoda kanał w góre
    def canal_up(self):
        self.canal +=1
        if self.canal >=10:
            self.canal = 10

    # metoda kanał w dół
    def canal_down(self):
        self.canal -=1
        if self.canal == 1:
            self.canal = 1

    # metoda volume up
    def add_volume(self):
        self.volume += 1

    # metoda volume down
    def sub_volume(self):
        self.volume -= 1

    # metoda wyswietlenie obecnego statnu
    def talk(self):
        print("Obecny nr kanału to:",self.canal)
        print("Obecny poziom glosnosci to:",self.volume)


def main():

    # konkretyzacja obiektu
    televisor = Televison()

    # menu interaktywne
    choice = None
    while choice != "0":
        print(
            """Menu TV:
            
            0 - wyłącz
            1 - wyświetl aktualny kanał i gloscnosc
            2 - podglos
            3 - scisz
            4 - kanał w góre
            5 - kanał w dół
            """
        )

        choice = input("Co wybierasz?: ")
        if choice == "0":
            print("Telewizor wyłaczony")
        elif choice == "1":
            televisor.talk()
        elif choice == "2":
            televisor.add_volume()
        elif choice == "3":
            televisor.sub_volume()
        elif choice == "4":
            televisor.canal_up()
        elif choice == "5":
            televisor.canal_down()

        else:
            print("Nieprawidlowy wybór")

# wywołanie programu
main()