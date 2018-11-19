import karty, gry

class BJ_Card(karty.Card):
    """Karta do blackjacka"""
    ACE_VALUE = 1

    @property
    def value(self):
        if self.face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
            else:
                v = None
            return v


class BJ_Deck(karty.Deck):
    """Talia kart do blackjacka"""
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))


class BJ_Hand(karty.Hand):
    """Ręka w blackjacku"""
    def __init__(self, name):
        super(BJ_Hand,self).__init__()
        self.name = name


    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep


    @property
    def total(self):
        # jeśli karta w ręce ma wartość none to i suma wynosi None
        for card in self.cards:
            if not card.value:
                return None

        # zsumuj wartości kart, traktuj każdego asa jako 1
        t = 0
        for card in self.cards:
            t += card.value

        # ustal czy reka zawiera asa
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True

        # jeśli reka zawiera asa, a suma jest wystarczajaco niska
        # potraktuj asa jako 11
        if contains_ace and t <= 11:
            t += 10

        return t

    def is_busted(self):
        return self.total > 21

class BJ_Player(BJ_Hand):
    """Gracz w blackjacku"""
    def is_hitting(self):
        response = gry.ask_yes_no("\n" + self.name + ", czy chcesz dobrać kartę (T/N): ")
        return response == "t"

    def bust(self):
        print(self.name, "ma fure")
        self.lose()

    def lose(self):
        print(self.name, "przegrywa")

    def win(self):
        print(self.name, "wygrywa")

    def push(self):
        print(self.name, "wygrywa")


class BJ_Dealer(BJ_Hand):
    """Rozdajacy w blackjacku"""
    def is_hittng(self):
        return self.total < 17

    def bust(self):
        print(self.name, "ma fure")

    def flip_first_card(self):
        first_card = self.cards[0]
        first.card.flip()



class BJ_Game(object):
    """Gra w blackjacka"""
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer("Rozdający")

        self.deck = BJ_Deck
        self.deck.populate()
        self.deck.shuffle()


    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                player.bust()
        return sp


    def __additional_cards(self, player):
            while not player.is_busted() and player.is_hitting():
                self.deck.deal([player])
                print(player)
                if player.is_busted():
                    player.bust()

    def play(self):
        # rozdaj każdemu początkowe dwie karty
        self.deck.deal(self.players + [self.dealer], per_hand= 2)
        self.dealer.flip_first_card() # ukryj pierwsza karte rozdającego
        for player in self.players:
            print(player)
        print(self.dealer)

        #rozdaj dodatkowe karty
        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card() # odsłoń pierwsza karte rozdającego

        if not self.still_playing:
            print(sef.dealer)
        else:
            # daj dodatkowe atrybuty rozdajacemu
            print(self.dealer)
            self.__additional_cards(self.dealer)

        if self.dealer.is_busted():
            # wygrywa ten kto pozostaje w grze
            for player in self.still_playing:
                player.win()

        else:
            for player in self.still_playing:
                if player.total > self.dealer.total:
                    player.win()
                elif player.total < self.dealer.total:
                    player.lose()
                else:
                    player.push()

        for player in self.players:
            player.clear()
        self.dealer.clear()



def main():
    print("Gra blackjack:")

    names = []
    numbers = gry.ask_number("Podaj liczbe graczy 1-7", low = 1, high = 8)
    for i in range(numbers):
        name = str(input("Wprowadz nazwe gracza"))
        names.append(name)
    print()

    game = BJ_Game(names)

    again = None
    while again != "n":
        game.play()
        again = gry.ask_yes_no("Chcesz grac ponownie?: ")

main()