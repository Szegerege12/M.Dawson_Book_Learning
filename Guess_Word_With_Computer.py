### Gra w ktorej komputer wybiera slowo ze stalej, ktore gracz musi odgadnac na podstawie liter
### import modulu random wykorzystywanego do losowania slow
import random

### deklaracja stalej zawierajaca slowa
WORDS = ("pterodaktyl","brontozaur","szlachcic","kuternoga","kanapka")

### slowo do odgadniecia jest losowe
word = random.choice(WORDS)

### informacja ile liter ma slowo
print("Slowo wybrane przez komputer ma dlugosc",len(word),"znakow")

### ustawienie petli na 4 mozliwosci zapytania o literke wystepujaca w slowie
counter = 0
while counter < 4:
    char = str(input("Zapytaj o litere"))
    if char in word:
        print("Tak")
    else:
        print("Nie")
    counter += 1


# pora na odpowiedz
answer = str(input("Pora na odgadniecie hasla: "))
if answer == word:
    print("Wygrales")
else:
    print("Przegrana")
