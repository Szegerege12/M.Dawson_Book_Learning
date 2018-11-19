import gry
class Card(object):
    """Karta do gry karcianej Wojna"""
    # figury
    RANK = ["9","10", "J", "D", "K", "A"]
    # kolory
    SUITS = ["d", "w", "c", "ż"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

    @property
    def value(self):
        if self.rank:
            v = Card.RANK.index(self.rank) + 10
        else:
            v = None
        return v

class Hand(object):
    """Ręka gracza"""
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "reka pusta"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, hand):
        self.cards.remove(card)
        hand.add(card)

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None
        t = 0
        for card in self.cards:
            t += card.value
        return t


class Deck(Hand):
    """Talia kart"""
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANK:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)


    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)


def wargame():
    print("Witaj w grze wojna\n")
    player1 = Hand()
    player2 = Hand()
    hands = [player1, player2]
    print("Oto talia kart:\n")
    deck = Deck()
    deck.populate()
    print(deck)
    print("tasuje talie...\n")
    deck.shuffle()
    print(deck)
    print("Rozdaję karty obu graczom...\n")
    deck.deal(hands= hands, per_hand= 1)
    print("Gracz pierwszy ma kartę:",player1, "o wartości punktowej:",player1.total)
    print("Gracz drugi ma kartę: ",player2, "o wartości punktowej:",player2.total)
    if player1.total > player2.total:
        print("Gracz pierwszy wygrywa")
    elif player2.total > player1.total:
        print("Gracz drugi wygrywa")
    else:
        print("remis")


def main():
    print("Witaj w grze wojna dla dwóch osób")

    choice = None
    while choice != "2":
        print("""
        1 - graj w wojne
        2 - zakończ
        """)
        wargame()
        choice = input("Jaki jest Twój wybór?: ")


main()