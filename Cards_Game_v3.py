class Card(object):
    """Karta do gry"""
    # figury
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
    # kolory
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Unprintable_Card(Card):
    """Karta której kolor i ranga nie zostaja ujawnione"""
    # przesłanianie metody klasy bazowej, ponowne jej wywolanie w klasie pochodnej tzn. jej deklaracja
    def __str__(self):
        return "<utajniona>"


class Positionable_Card(Card):
    """karta która może być odkrytka lub zakryta"""
    def __init__(self, rank, suit, face_up = True):
        super(Positionable_Card, self).__init__(rank,suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super(Positionable_Card, self).__str__()
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up


# Część główna
card1 = Card("A","c")
card2 = Unprintable_Card("A","d")
card3 = Positionable_Card("A","h")

print("Wyświetlenie obiekty klasy Csrd:")
print(card1)

print("Wyświetlenie obiektu klasy Unprintable_Card:")
print(card2)

print("Wyświetlenie obiekt klasy Positionable_Card:")
print(card3)

print("Odwracam karte nr 3")
card3.flip()

print("Ponowne wyświetlenie obiekty klasy Positionable_Card:")
print(card3)

input("\nAby zakończyć działanie programu naciśnij klawisz Enter.")