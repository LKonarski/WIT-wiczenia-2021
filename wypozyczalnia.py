#zad5

#1). Utwórz użytkownika
#2). Dodaj film
#3). Zmodyfikuj ilość dostępnego filmu
#4). Zobacz całą ofertę
#5). Sprawdź dostępność filmu
#6). Wypożycz film
#7). Zaloguj się
#0). Wyjdź z programu

is_authenticated = False
movies = {}
users = {}

def register_user():
    login = input('Wprowadź swój login: ')
    password = input('Wprowadź swoje hasło: ')
    users[login] = password
    print(users)

def add_movie():
    film_name = input('Wprowadź nazwę filmu: ')
    amount = int(input('Wprowadź ilość dotępnych kopii filmu: '))
    movies[film_name] = amount

def modify_movie():
    film_name = input('Wprowadź nazwę filmu: ')
    if movies.get(film_name):
        new_amount = int(input('Wprowadź nową ilość dotępnych kopii filmu: '))
        movies[film_name] = new_amount
        print(movies)
        return movies.get(new_amount)
    else:
        print('Podana nazwa filmu jest nieprawidłowa')

def get_movies():
    for i in movies:
        print(i, movies[i])

def check_movie_availability():
    film_name = input('Wprowadź nazwę filmu: ')
    if movies.get(film_name):
        if movies[film_name] >= 1:
            print('Dostępna jest co najmniej 1 sztuka filmu')
        else:
            print('Obecny film jest niedostępny')
    else:
        print('Podana nazwa filmu jest nieprawidłowa')

def rent_movie():
    film_name = input('Wprowadź nazwę filmu: ')
    if movies.get(film_name) and movies[film_name] >= 1:
        movies[film_name] = movies[film_name] - 1
        print(movies, 'Wypożyczono film')
    else:
        print('Nie udało się wypożyczyć filmu')
        
def login_user():
    login = input('Wprowadź swój login: ')
    password = input('Wprowadź swoje hasło: ')
    if users.get(login) == password:
        is_authenticated = True
        print('Zalogowano pomyślnie')
    else:
        is_authenticated = False
        print('Niepoprawne dane logowania')
        exit()

while True:
    print('1). Utwórz użytkownika')
    print('2). Dodaj film')
    print('3). Zmodyfikuj ilość dostępnego filmu')
    print('4). Zobacz całą ofertę')
    print('5). Sprawdź dostępność filmu')
    print('6). Wypożycz film')
    print('7). Zaloguj się')
    print('0). Wyjdź z programu')

    option = input('Wybierz opcję: ')

    if option == '1':
        register_user()
    elif option == '2':
        login_user()
        add_movie()
    elif option == '3':
        login_user()
        modify_movie()
    elif option =='4':
        get_movies()
    elif option == '5':
        check_movie_availability()
    elif option == '6':
        login_user()
        rent_movie()
    elif option == '7':
        login_user()
    elif option == '0':
        break