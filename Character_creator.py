# Kreator postaci
# Uzytkownik ma możliwośc zbudowania swojego bohatera posiadajac do rozdania 30 pkt statystyk
# Moze je rozdzielic pomiedzy sile,zdrowie,madrosc,zrecznosc
# Gracz ma mozliwosc przeznaczenia pkt na dowolny atrybut jak i mozliwosc odbierania

# deklaracja tablicy w ktorej przechowywane zostana atrybuty

total = 30
choice = None



ATTRIBUTES = ("siła",
              "zdrowie",
              "madrosc",
              "zrecznosc")
scores = {
    ATTRIBUTES[0]: 0,
    ATTRIBUTES[1]: 0,
    ATTRIBUTES[2]: 0,
    ATTRIBUTES[3]: 0,
}
while choice != "0":
    print(
    """
    Kreator postaci. Masz mozliwosc rozdania 30 pkt statystyk
    Dostepne atrybuty: siła, zdrowie, mądrość, zręczność
    
    0 - zakończ działanie programu
    1 - wyświetl stan dostepnych punktów do rozlowkowania
    2 - dodaj atrybuty bohaterowi
    3 - zmień atrybuty bohatoerowi
    4 - obecny stan statysyk
    """
    )
    # wybór opcji
    choice = input("Wybierasz: ")
    # zakonczenie programu
    if choice == "0":
        print("Kreator konczy prace")

    # wyswietlenie aktualnego stanu pkt do rozdania w puli
    elif choice == "1":
        print("Stan punktów do rozdania wynosi:",total)

    # dodanie pkt do wybranego atrybutu
    elif choice == "2" and total >=0:
        print(ATTRIBUTES)
        choice = int(input("Wprowadz indeks atrybutu do którego chcesz dodac pkt( od 0 do 3: "))
        stat = ATTRIBUTES[choice]
        print("Wybrales",stat)
        points = int(input("Ile punktów chcesz dodać do attrybutu: "))
        scores[stat] += points
        total -= points
        print("Pozostalo Ci",total,"punktów do rozdania")
        input("\nNacisnij klawisz enter aby powrócić do menu.")



    #przywracanie pkt do wartosci total
    elif choice == "3":
        print(ATTRIBUTES)
        choice = int(input("Wprowadz indeks atrybutu od którego chcesz odjac pkt( od 0 do 3: "))
        stat = ATTRIBUTES[choice]
        print("Wybrales",stat)
        points = int(input("Ile punktów chcesz usunąc z atrybutu:" ))
        scores[stat] -=points
        total =+ points
        print("Aktualnie masz",total,"punktów do rozdania")
        input("Aby powrócić do menu głównego naciśnij klawisz Enter.")


    #wyswietlanie aktualnych statystyk
    elif choice == "4":
        print("Aktualne statystyki:")
        print(scores)
else:
    print("Nie masz tyle punktów")


