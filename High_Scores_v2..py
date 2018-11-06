### Najlepsze wyniki 2.0
### Uzycie sekwencji zagniezdzonych
scores = []
choice = None
while choice != '0':
    print(
    """
    Najlepsze wyniki 2.0
    
    0 - zakończ
    1 - wyświetl wyniki
    2 - dodaj wyniki
    """
    )
    choice = input("Wybierasz: ")
    if choice == '0':
        print("Do zobaczenia")
    # wyświetl tabele najlepszych wyników
    elif choice == '1':
        print("Najlepsze wyniki\n")
        print("GRACZ|WYNIK")
        for entry in scores:
            score, name = entry
            print(name,"\t",score)
    #dodanie wyniku do listy
    elif choice == '2':
        name = input("Podaj nazwe gracza: ")
        score = int(input("Podaj wynik gracza: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5] # zachowuj tylko 5 najlepszych wynikow
    else:
        print(choice,"Wybor nie prawidlowy")

input("\n\nAby zakonczyc dzialanie programu nacisnij klawisz Enter.")