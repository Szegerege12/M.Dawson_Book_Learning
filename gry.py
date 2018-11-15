# Moduł Gry
# Demonstracja tworzenie modułu

class Player(object):
    """Uczestnik gry"""
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name +":\t" + str(self.score)
        return rep


def ask_yes_no(question):
    """Zadaje pytania na ktore mozna odpowiedziec tak lub nie"""
    response = None
    while response not in ('t','n'):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Prosi o podanie liczby z podanego zakresu"""
    response = None
    while response not in range(low, high):
        response = int(input(question).lower())
    return response


if __name__ == "__main__":
    print("Uruchomiles program bezpośrednio. Powinieneś importować moduł")