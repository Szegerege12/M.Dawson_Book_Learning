# Turniej wiedzy
# Gra odczytujaca dane ze zwyklego pliku tekstoweog

import sys, pickle

def open_file(file_name, mode):
    """
    Otwiera plik tekstowy
    :param file_name:
    :param mode:
    :return:
    """
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Nie można otworzyć pliku", file_name,"program zostanie zakończony\n")
        input("\n Aby zakończyć działnie programu, naciśnij klawisz enter,")
        sys.exit()
    else:
        return the_file


def next_line(the_file):
    """
    Zwróć kolejny wiersz pliku kwiz po sformatowaniu go.
    :param the_file:
    :return:
    """
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line


def next_block(the_file):
    """
    Zwraca cały blok z kategoria, pytaniem, odpowiedziami i objasnieniem
    :param the_file:
    :return:
    """
    category = next_line(the_file)
    question = next_line(the_file)

    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    points = next_line(the_file)
    explanation = next_line(the_file)

    return category, question, answers, correct, points, explanation


def welcome(title):
    """
    Wita gracza i zwraca tytul odcinka
    :param title:
    :return:
    """
    print("Witaj w tutnieju wiedzy\n")
    print("Tytul odcinka to:",title)


def add_score(name,score):
    """
    Dodaje wynik do osobnego pliku txt.
    :param name:
    :param score:
    :return:
    """
    f = open("scores_game.dat", "ab")
    my_list = []
    scores = (name,score)
    my_list.append(scores)
    pickle.dump(my_list, f)
    f.close()


def main():
    trivia_file = open_file("quiz.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    # pobierz pierwszy blok
    category, question, answers, correct, points, explanation = next_block(trivia_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print("\t",i + 1,"-", answers[i])

        answer = input("Jaka jest Twoja odpowiedz?: ")
        if answer == correct:
            print("Odpowiedz prawidłowa", end = " ")
            score = score + int(points)
        else:
            print("Odpowiedz nieprawidlowa", end = " ")
        print(explanation)
        print("Wynik:",score)

        category, question, answers,  correct, points, explanation = next_block(trivia_file)

    trivia_file.close()
    print("To koniec pytan. Twój wynik to:",score)
    name = str(input("Podaj swoje imie: "))
    add_score(name,score)


main()
print("Wyniki gry:")
f = open("scores_game.dat", "rb")
my_list = pickle.load(f)
print(len(my_list))
print(my_list)
f.close()