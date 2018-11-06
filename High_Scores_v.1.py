### program pokazujacy wlasciwosci listy
### High_Scores

scores = []
choice = None
### petla bedzie dzialac dopóki wybór nie padnie na 0
while choice != 0:
    print(
    """
    Najlepsze wyniki
    
    0 - zakoncz
    1 - pokaż wyniki
    2 - dodaj wynik
    3 - usuń wynik
    4 - posortuj wyniki
    """
    )
    ### Wybór opcji z menu
    choice = input("Wybierasz: ")
    print()
    if choice == '0':
        print("Do zobaczenia")
        break
    ### wyswietla wyniki
    elif choice == '1':
        print("Najlepsze wyniki")
        for score in scores:
            print(score)
    ### dodaje wynik do listy scores
    elif choice == '2':
        score = int(input("Jaki wynik uzyskales?: "))
        scores.append(score)
    ### usuwanie wyniku z listy scores
    elif choice == '3':
        score = int(input("Który wynik usunać?: "))
        if score in scores:
            scores.remove(score)
        else:
            print(score,"Nie ma na liscie wynikow")
    elif choice == '4':
        scores.sort(reverse=True)
    ### nieznana opcja
    else:
        print("Niestety, ale",choice,"jest nieprawidlowym wyborem")

input("\n\Aby zakonczyc dzialanie programu nacisnij klawisz Enter")