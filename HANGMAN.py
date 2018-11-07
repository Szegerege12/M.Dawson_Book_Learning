# Szubienica - gra

import random
#stałe
HANGMAN = (
    """
    --------
    |       |
    |
    |
    |
    |
    |
----------
    """,
    """
     --------
    |       |
    |       0
    |
    |
    |
    |
----------
    """,
    """
     --------
    |       |
    |       0
    |       +
    |
    |
    |
----------
    """,
    """
     --------
    |       |
    |       0
    |      \+
    |
    |
    |
----------
    """,
    """
     --------
    |       |
    |       0
    |      \+/
    |
    |
    |
----------
    """,
    """
    --------
    |       |
    |       0
    |      \+/
    |      |
    |
    |
----------
    """,
    """  
    --------
    |       |
    |       0
    |      \+/
    |      | |
    |
    |
----------"""
)

MAX_WRONG = len(HANGMAN) - 1                                    #maks liczba nieprawidlowych odpowiedzi
WORDS = ("CISOWIANKA","PSZCZOŁA","WIANEK","TAKSÓWKA","PYTHON")  #slowa uzywane w grze
word = random.choice(WORDS)                                     #wybor slowa randomowo
so_far = "-" * len(word)                                        #slowo zakreskowane
wrong = 0                                                       #liczba zlych odpowiedzi
used = []                                                       #uzyte juz litery

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nWykorzystales juz nastepujace litery:\n",used)
    print("\nNa razie zagadkowe slowo wyglada tak:\n",so_far)

    guess = input("\nWprowadz litere: ")
    guess = guess.upper()

    while guess in used:
        print("Juz wykorzystales litere",guess)
        guess = input("\nWprowadz litere: ")
        guess = guess.upper()
    used.append(guess)

    if guess in word:
        print("Tak, podana litera jest w zagadkowym słowie")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new+= so_far[i]
        so_far = new
    else:
        print("Niestety litera",guess,"nie wystepuje w zagadkowym slowie.")
        wrong += 1
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("Zostales powieszony")
else:
    print("Odgadles")
print("Zagadkowe slowo to",word)