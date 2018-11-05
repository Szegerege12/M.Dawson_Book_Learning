### importowanie modulu random
import random

### deklaracja STAŁEJ
WORDS = ("python","anagram","łatwy","skomplikowany","odpowiedź","ksylofon")

word = random.choice(WORDS)
correct = word
jumble = ""

#konfiguracja petli tak by program wykonywany byl dotad az wartosc zmiennej word nie bedzie rowna pustemu lancuchowi
while word:
    position = random.randrange(len(word)) # losowa pozycja w lancuchu na podstawie jego dlugosci
    jumble += word[position]               # dodaje literke do nowego wiersza
    word = word[:position] + word[(position +1):] # tworzy word bez tej jednej literki

print("Zgadnij co to za słowo:",jumble)
guess = input("\nTwoja odpowiedz: ")
while guess != correct and guess !="":
    print("Niestety to nie to slowo: ")
    guess = input("Twoja odpowiedz")

    if guess == correct:
        print("Gratulacje, odgadłes anagram")