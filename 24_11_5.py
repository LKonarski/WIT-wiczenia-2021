slownik = {}

def print_menu():
    print('1. Dodaj wpis')
    print('2. Odzyskaj wpis')
    print('3. Zmodyfikuj wpis')
    print('4. Usuń wpis')
    print('0. Wyjdź')
    
def create_item():
    item = input('Wprowadź wpis: ')
    value = input('Wprowadź wartość w str: ')
    slownik[item] = value

def read_item():
    item  = input('Wprowadź wpis: ')
    if slownik.get(item):
        print(slownik[item])
    else:
        print('Podane wpis jest niepoprawny')

def update_item():
    item = input('Wprowadź wpis: ')
    if slownik.get(item):
        new_item = input('Wprowadź nowy wpis: ')
        slownik[item] = new_item
        print(slownik)

def delete_item():
    item = input('Wprowadź wpis: ')
    if slownik.get(item):
        pass

while True:
    print_menu()
    option = input('Podaj opcję: ')
    if option == '1':
        create_item()
    elif option == '2':
        read_item()
    elif option == '3':
        update_item()
    elif option == '4':
        delete_item()
    elif option == '0':
        break