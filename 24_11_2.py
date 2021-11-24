def check_parity():
    number = int(input('Podaj liczbę: '))
    if number % 2 == 0:
        print('Podana liczba jest parzysta')
    else:
        print('Podana liczba jest nieparzysta')

check_parity()