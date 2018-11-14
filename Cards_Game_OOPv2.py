"""
Gra w karty
Demonstruje tworzenie kombinacji obiektów
"""

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


class Hand(object):
    """ Ręka - karty do gry w ręku gracza"""

    # lista obiektów klasy Cards(zamierzona)
    def __init__(self):
        self.cards = []

    # wyswietlanie łancucha znaków ukazującego kary w ręce
    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t "
        else:
            rep = "<pusta>"
        return rep

    # kasuje liste kart poprzez przypisanie pustej listy
    def clear(self):
        self.cards = []

     # dodaje obiekt do atrybutu cards
    def add(self, card):
        self.cards.append(card)

     # usuwa od siebie daje innemu
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

# talia kart, klasa pochodna z klasy Hand, dziedzizy jej metody
class Deck(Hand):
    """Talia kart do gry"""
    # zapełnienie talii kart
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    # tasowanie
    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Nie moge dalej rozdawac zabraklo kart")
deck1 = Deck()
print(deck1)
deck1.populate()
print(deck1)
deck1.shuffle()
print(deck1)

my_hand = Hand()
your_hand = Hand()
hands = [my_hand, your_hand]

deck1.deal(hands,per_hand=5)
print(my_hand)
print(your_hand)