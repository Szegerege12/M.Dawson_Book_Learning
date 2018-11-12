import random


def ask_number():
    """
    Guess the number form range
    :return:
    """
    the_number = random.randint(1,10)
    guess = int(input("Podaj liczbe w przedziale 1:10. Masz 4 szanse: "))
    count = 1

    while count < 4:
        if guess != the_number:
            if guess > the_number:
                print("Podana liczba jest za duża")
            else:
                print("Podana liczba jest za mała")
        guess = int(input("Podaj liczbe w przedziale 1:10.: "))
        count +=1
        if guess == the_number:
            print("Gratulacje. Odgladles poprawna liczbe w",count,"podejsciu")
            break
        elif count == 4:
            print("Koniec wykorzystaleś liczbe prób")
            break

def main():
    """
    Main function
    :return:
    """
    ask_number()


main()

