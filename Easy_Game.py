# Prosta gra w której importuje wcześniej utworzony przez siebie moduł

import gry, random


print("Witaj w prostej grze która używa modułu który sam napisałem!")

choice = None
while choice != 'n':
    players = []
    num = gry.ask_number(question = "Podaj liczbę graczy od 2 do 5:", low = 2, high= 5)

    for i in range(num):
        name = input("Podaj Nazwe gracza: ")
        score = random.randrange(100) + 1
        player = gry.Player(name,score)
        players.append(player)


    print("\nWyniki:")
    for player in players:
        print(player)

    choice = gry.ask_yes_no("Czy chcesz grać dalej? <t/n>")
