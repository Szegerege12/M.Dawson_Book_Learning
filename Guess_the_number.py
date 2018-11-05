### jaka to liczba
import random

### ustawianie wartosci poczatkowych
the_number = random.randint(1,5)
guess = int(input("Podaj liczbe do zgadniecia od 1 do 5"))
count = 1

### stworzenie petli zgadywania(bez konca dopoki wartosc nie jest odgadnieta)

while count < 4:
    if guess != the_number:
        if guess > the_number:
            print("Podana liczba jest za duża.")
        else:
            print("Podana liczba jest za mala.")

    guess = int(input("Podaj liczbe do zgadniecia od 1 do 5: "))
    count += 1
    if guess == the_number:
        print("Gratulacje. Poprawna liczba. Odgadles poprawna liczbe w podejsciu nr",count)
        break
    elif count == 4:
        print("Koniec prób. Koniec gry.")
        break




