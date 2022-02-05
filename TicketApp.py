from multiprocessing import connection
import sqlite3

class Developer():
    def register_developer():
        login = input('Wprowadź swój login: ')
        password = input('Wprowadź swoje hasło: ')
        connection = sqlite3.connect('baza_danych.db')
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS developers (login, password)')
        cursor.execute('INSERT INTO developers VALUES (?, ?)', (login, password))
        connection.commit()
        connection.close()
        print(login, password)

    def update_maps():
        region = input('Wprowadź nazwę nowego regionu: ')
        size = int(input('Wprowadź rozmiar danego obszaru: '))
        connection = sqlite3.connect('baza_danych.db')
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS maps (region, size)')
        cursor.execute('INSERT INTO maps VALUES (?, ?)', (region, size))
        connection.commit()
        connection.close()
        print(region, size)


    def user_help():
        print('Witam z tej strony asystent, zapoznałem się z problemem, pracujemy nad tym!')
        
class User():
    def register_user():
        login = input('Wprowadź swój login: ')
        password = input('Wprowadź swoje hasło: ')
        connection = sqlite3.connect('baza_danych.db')
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS users (login, password)')
        cursor.execute('INSERT INTO users VALUES (?, ?)', (login, password))
        connection.commit()
        connection.close()
        print(login, password)


    def get_wallet():
        print('''Wybierz czynność:
        1. Doładuj wirtualny portfel
        2. Sprawdź zawartość wirtualnego portfela''')
        option = int(input('Wybierz opcje: '))

        if option == 1:
            money = input('Wprowadź nazwę waluty: ')
            amount = int(input('Wprowadź ilość pieniędzy jaką chcesz przelać: '))
            connection = sqlite3.connect('baza_danych.db')
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS wallet (money, amount)')
            cursor.execute('INSERT INTO wallet VALUES (?, ?)', (money, amount))
            connection.commit()
            connection.close()
            print(money, amount)

        if option == 2:
            connection = sqlite3.connect('baza_danych.db')
            cursor = connection.cursor()
            queryset = cursor.execute('SELECT * FROM wallet')
            print(queryset.fetchall())

    def get_tickets():
        print('''Wybierz rodzaj biletu
        1. Bilet na autobus
        2. Bilet na pociąg
        3. Bilet na samolot''')
        option = int(input('Wybierz opcje: '))

        if option == 1:
            print('Kupujesz bilet na autobus, aktualny cennik to 1$ za 10 minut')
            time = int(input('Wprowadź ile czasu w minutach będziesz podróżował: '))
            result = time/10
            connection = sqlite3.connect('baza_danych.db')
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS tickets (time, result)')
            cursor.execute('INSERT INTO tickets VALUES (?, ?)', (time, result))
            connection.commit()
            connection.close()
            print('Koszt przejazdu wynosi: ', result,'$')
        
        if option == 2:
            print('Kupujesz bilet na pociag, aktualny cennik to 5$ za 60 minut')
            time = int(input('Wprowadź ile czasu w minutach będziesz podróżował: '))
            result = time/60*5
            connection = sqlite3.connect('baza_danych.db')
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS tickets (time, result)')
            cursor.execute('INSERT INTO tickets VALUES (?, ?)', (time, result))
            connection.commit()
            connection.close()
            print('Koszt przejazdu wynosi: ', result,'$')
            

        if option == 3:
            print('Kupujesz bilet na samolot, aktualny cennik to 50$ za 60 minut')
            time = int(input('Wprowadź ile czasu w minutach będziesz podróżował: '))
            result = time/60*50
            connection = sqlite3.connect('baza_danych.db')
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS tickets (time, result)')
            cursor.execute('INSERT INTO tickets VALUES (?, ?)', (time, result))
            connection.commit()
            connection.close()
            print('Koszt przejazdu wynosi: ', result,'$')
            

    def show_tickets():
        connection = sqlite3.connect('baza_danych.db')
        cursor = connection.cursor()
        queryset = cursor.execute('SELECT * FROM tickets')
        print(queryset.fetchall())

    def return_tickets():
        connection = sqlite3.connect('baza_danych.db')
        cursor = connection.cursor()
        queryset = cursor.execute('SELECT * FROM tickets')
        print(queryset.fetchall())       

    
    def check_maps():
        connection = sqlite3.connect('baza_danych.db')
        cursor = connection.cursor()
        queryset = cursor.execute('SELECT * FROM maps')
        print(queryset.fetchall())

    def contact():
        x = input('Wprowadź swój problem: ')
        print('Łączenie z asystentem...')

print('TicketApp')

print('''Wybierz opcje zalogowania na konto
1.Zaloguj jako użytkownik
2.Zaloguj jako deweloper''')
option = int(input('Wybierz opcje: '))

if option == 1:
    print('Logowanie na konto klienta')
    User.register_user()
    
    while True:
        print('''Opcje do wyboru:
        1. Witrualny portfel
        2. Kupno biletów
        3. Pokazanie zawartości skrytki z posiadanymi biletami
        4. Zwrot biletów
        5. Mapy
        6. Kontakt z asystentem
        7. Zakończ program''')
        choice = int(input('Wybierz jedną z opcji: '))

        if choice == 1:
            User.get_wallet()
        if choice == 2:
            User.get_tickets()
        if choice == 3:
            User.show_tickets()
        if choice == 4:
            User.return_tickets()
        if choice == 5:
            User.check_maps()
        if choice == 6:
            User.contact()
        if choice == 7:
            print('Wylogowano pomyślnie')
            break

if option == 2:
    print('Logowanie na konto jako deweloper')


    while True:
        print('''Opcje do wyboru:
        1. Zaaktualizuj mapy
        2. Pomoc dla klienta
        3. Zakończ program''')
        choice = int(input('Wybierz jedną z opcji: '))
        
        if choice == 1:
            Developer.update_maps()
        if choice == 2:
            Developer.user_help()
        if choice == 3:
            print('Wylogowano pomyślnie')
            break
