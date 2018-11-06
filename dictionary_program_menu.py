### program prezentujacy zastosowanie slownika
#tworzenie slownika {}
dictionary = {"404":"błąd komputerowy w sieci",
              "google":"najpopularniejsza szukajka internetowa",
              "instalacja":"proces wgrywania jakiegos pgoramu"}

#tworzenie menu programu
choice = None
while choice !="0":
    print(
        """
        Translator slangu komputerowego
        
        0 - zakończ program
        1 - znajdź termin
        2 - dodaj nowy termin
        3 - zmień definicje terminu
        4 - usuń termin
        """
        )
    choice = input("Co wybierasz: ")
    if choice == "0":
        print("Do zobaczenia")

    #wyswietlanie definicji 
    elif choice == "1":
        term = input("Jaka definicje mam przetlumaczyc?: ")
        if term in dictionary:
            definition = dictionary[term]
            print("\n",term,"oznacza",definition)
        else:
            print("Niestety, nie znam terminu",term)

    #dodaj termin-definicja
    elif choice == "2":
        term = input("Jaki termin mam dodać?: ")
        if term not in dictionary:
            definition = input("Podaj definicje terminu")
            dictionary[term] = definition
            print("\nTermin",term,"został dodany")
        else:
            print("\nPodany termin juz istnieje, sproboj zmienic jego definicje")

    #zmiana definicji istniejacego terminu
    elif choice == "3":
        term = input("Który termin zmienic definicje?: ")
        if term in dictionary:
            definition = input("Jaka ma byc nowa definicja?: ")
            dictionary[term] = definition
            print("\nNowa definicja zostala przypisana")
        else:
            print("Podanego terminu nie ma w slowniku. Spróbój go najpierw dodac.")

    #usuniecie pary term/def
    elif choice == "4":
        term = input("Który termin chcesz usunac?: ")
        if term in dictionary:
            del dictionary[term]
            print("\nTermin",term,"usuniety ze slownika")
        else:
            print("Nie moge tego zrobic.",term,"nie wystepuje w slowniku")
    else:
        print("Nieprawidlowy wybór.")
input("\n\nAby zakonczyć działanie programu nacisnij klawisz Enter")


