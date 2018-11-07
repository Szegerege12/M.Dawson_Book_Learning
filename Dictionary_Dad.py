# Program kto jest Twoim tatą
# Umozliwia uzytkownikowi wprowadzenie imienia i nazwiska osoby płci meskiej i przedstawia imie i nazwisko jej ojca

names = {"Adam Małysz":"Julian Podlaski",
         "Kaja Paschalska:":"Mojzesz"}

choice = None
while choice != "0":
    print(
        """
        Słownik komputerowy imion dzieci i ojców
        
        0 - Zakończ program
        1 - Znajdz termin
        2 - Dodaj nowy rekord
        3 - Usuń rekord
        """
    )
    choice = input("Co wybierasz: ")
    if choice == "0":
        print("Zakończenie programu")
    if choice == "1":
        name = str(input("Czyjego rodzica chcesz znac, podaj pełne imie i nazwisko: "))
        if name in names:
            father = names[name]
            print("Ojciec",name,"to",father)
        else:
            print("Podanego imienia nie ma w slowniku")
    elif choice == "2":
        name = str(input("Jaka osobe chcesz dodac do slownika?: "))
        if name not in names:
            father = str(input("Podaj ojca tej osoby: "))
            names[name] = father
            print("Osoba",name,"została dodana do rejetru")
        else:
            print("Osoba jest już w rejestrze")
    elif choice == "3":
        name = str(input("Podaj dane osoby do usuniecia z rejestru: "))
        if name in names:
            del names[name]
        else:
            print("Podanej osoby nie ma w rejestrze")


input("\n\nAby zakończyc działanie programu nacisnij klawisz Enter.")
