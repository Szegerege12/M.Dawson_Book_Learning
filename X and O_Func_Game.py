# Kółko i krzyżyk z wykorzystaniem AI

#Stałe globalne
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9
# Funkcje

def display_instruct():
    """
    Wyświetla instrukcje do gry kółko i krzyżyk
    :return:
    """
    print(
        """
        Witaj w grze kółko i krzyżyk.
        Swoje posuniecia wskazesz poprzez wprowadzanie liczby z zakresu 0-8.
        Liczba odpowiada pozycji na planszy zgodnie z poniższym schematem.
        
        0  |  1  |  2
        -------------
        3  |  4  |  5
        -------------
        6  |  7  |  8
        """
    )
def ask_yes_no(question):
    """
    Zadaje pytanie na które mozna odpowiedzieć tak lub nie
    :param question:
    :return:
    """
    response = None
    while response not in("t","n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """
    Prosi o podanie liczby z danego zakresu
    :param question: 
    :param low: 
    :param high: 
    :return: response:
    """
    response = None
    while response not in(low, high,):
        response = int(input(question))
    return response

def pieces():
    """
    Ustala czy pierwszy ruch należy do gracza czy do komputera. Pierwszy ruch w XO to X.
    :return:
    """
    go_first = ask_yes_no("Czy chcesz mieć prawo do pierwszego ruchu?<t/n>: ")
    if go_first == "t":
        print("\nPierwszy ruch należy do Ciebie.")
        human = X
        computer = O
    else:
        print("\Pierwszy ruch należy do komputera.")
        human = O
        computer = X
    return computer, human

def new_board():
    """
    Tworzy pustą planszę do gry
    :return:
    """
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """
    Wyświetla plansze do gry
    :param board:
    :return:
    """
    print(board[0], "|", board[1], "|", board[2])
    print("----------")
    print(board[3], "|", board[4], "|", board[5])
    print("----------")
    print(board[6], "|", board[7], "|", board[8])


def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    """
    Ustala zwyciezce gry
    :param board:
    :return:
    """
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None

def human_move(board, human):
    """
    Odczytuje ruch czlowieka
    :return:
    """
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Jaki bedzie Twoj ruch 0-8",0, NUM_SQUARES)
        if move not in legal:
            print("To pole jest zajete")
        print("znakomicie")
    return move

def computer_move(board, computer, human):
    """Sposoduj wykonanie ruchu przez komputer"""
# utwórz kopie roboccza poniewaz funkcja bedzie zmieniać liste
    board = board[:]
# najlepsze pozycie do zajecia według kolejnosci
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Wybieram pole numer", end=" ")
# jeśli komputer może wygrać wykonaj ten ruch
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY

    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

def next_turn(turn):
    if turn == X:
        return 0
    else:
        return X

def congrat_winner(the_winner, computer, human):
    if the_winner != TIE:
        print(the_winner, "jest zwyciezca!")
    else:
        print("Remis!\n")

    if the_winner == computer:
        print("Zwyciezca to komputer")

    elif the_winner == human:
        print("Zwycieza czlowiek")

    elif the_winner == TIE:
        print("remis")

def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board,computer,human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


# rozpocznij program
main()