#zad1
'''
print('Zarejestruj się')

def register():
    uzytkownicy = {}
    login = input('Wprowadź login: ')
    password = input('Wprowadź hasło: ')
    repeat_password = input('Wprowadź hasło ponownie: ')
    uzytkownicy[login] = password

    assert len(login) > 5, 'Login musi być dłuższy niż 5 znaków'

    if not len(password) > 6:
        raise ValueError('Hasło musi być dłuższe niż 6 znaków')
    if not password == repeat_password:
        raise ValueError('Oba hasła muszą być takie same')

    print(uzytkownicy)

register()
'''
#zad2
'''
def validate_list():
    list1 = [1, 2, 3, 4, 5]
    
    if list1 == []:
        raise ValueError('Lista jest pusta')

    for element in list1:
        assert isinstance(element, (int, float)), 'Elementy listy muszą być liczbą'

    return sum(list1), max(list1), min(list1)

print(validate_list())
'''
#zad3
'''
def log_app():
    uzytkownicy = {}

    while True:
        option = input("Podaj wybraną opcję: ")

        if option == '1':
            login = input('Wprowadź login: ')
            password = input('Wprowadź hasło: ')
            uzytkownicy[login] = password

        elif option == '2':
            for i in uzytkownicy:
                print(i, uzytkownicy[i])

        elif option == '3':
            login = input('Wprowadź login: ')
            if uzytkownicy.get(login):
                print('Użytkownik o tym loginie istnieje')
                new_password = input('Wprowadź nowe hasło: ')
                uzytkownicy[login] = new_password
                print(uzytkownicy)
                return uzytkownicy.get(new_password)
            else:
                print('Nie ma takiego użytkownika')
            
        elif option == '4':
            login = input('Wprowadź login: ')
            if uzytkownicy.get(login):
                uzytkownicy.clear()
                
            else:
                print('Nie ma takiego użytkownika')

        elif option == '5':
            break

log_app()
'''   
