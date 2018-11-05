# pobieranie od uzytkownika wartosci poczatkowej i koncowej i skoku
start = int(input("Podaj wartosc poczatkowa:"))
finish = int(input("Podaj wartosc koncowa:"))
jump = int(input("Wprowadz wielkosc odstepu miedzy liczbami"))

### przypisanie danych do zakresu
calc = range(start, finish, jump)
print(calc)

### wyswietlenie zadanego zakresu
for i in calc:
    print(i, end=" ")