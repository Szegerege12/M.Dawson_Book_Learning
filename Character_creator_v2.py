# Kreator postaci
# Uzytkownik ma możliwośc zbudowania swojego bohatera posiadajac do rozdania 30 pkt statystyk
# Moze je rozdzielic pomiedzy sile,zdrowie,madrosc,zrecznosc
# Gracz ma mozliwosc przeznaczenia pkt na dowolny atrybut jak i mozliwosc odbierania

#liczba pkt do rozdysponowania
total = 30

#atrybuty postaci
ATTRIBUTES = ("siła",
              "zdrowie",
              "mądrość",
              "zręczność")

#słownik w którym przechowujemy stan atrybutów
stats = {
    ATTRIBUTES[0]: 0,
    ATTRIBUTES[1]: 0,
    ATTRIBUTES[2]: 0,
    ATTRIBUTES[3]: 0
}

# start pętli
choice = None
while choice != "0":
    print(
        """
        Witaj w kreatorze postaci. Menu główne:
        
        0 - zakończ program
        1 - wyświetl liczbę wolnych punktów
        2 - dodaj punkty do atrybutu
        3 - odejmij punkty od atrybutu
        4 - wyświetl atrybuty postaci
        
        """
    )
    choice = input("Wybierz opcję: ")
    if choice == "0":
        print("Koncze prace kreatora")
# wyswietlanie wolnych punktów do rozdysponowania
    elif choice == "1":
        print("Liczba wolnych punktów to:",total)

# dodawanie punktów do atrybutu
    elif choice == "2" and total >=0:
        atr = int(input("Podaj ktory argument chcesz wybrac od 0 do 3: "))
        stat = ATTRIBUTES[atr]
        print("WWybrales atrybut",stat)

# sprawdzanie liczby pktów do dodania oraz warunku czy uzytkownik nie podał za duzo pktów
        points = int(input("Podaj liczbe punktów ktore chcesz dodac: "))
        if points > total:
            print("Masz za malo punktów")
        else:
            stats[stat] += points
            total =- points
            print("Dodano",points," pkt do atrybutu",stat)
            print("Pozostala liczba punktów do rozdysponowania to:",total)
            input("\nAby powrócic do menu naciśnij klawisz Enter")

# odejmowanie punktów od wybranego atrybutu
    elif choice == "3":
        atr = int(input("Podaj z którego argumentu chcesz odjac punkty od 0 do 3: "))
        stat = ATTRIBUTES[atr]
        print("Wybrales atrybut",stat)

        points = int(input("Ile pkt chcesz odjac?: "))
        stats[stat] =- points
        total =+ points
        print("Punkty dostepne do wykorzystania to teraz:",total)
        input("\nAby powrócic do menu naciśnij klawisz enter")

# wyswietlenie statystyk postaci
    elif choice == "4":
        print(stats)
        input("\nAby powrócic do menu naciśnij klawisz enter")
    else:
        print("Masz za malo punktów")

input("\nAby zakonczyc dzialanie programu naciśnij klawisz enter")
