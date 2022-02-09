import sqlite3
import datetime
import requests
from pprint import pprint

date = datetime.datetime.today()
conn = sqlite3.connect('numberapp.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users (username, password, requests_count)')
cursor.execute('CREATE TABLE IF NOT EXISTS users (username, data, type_param, number_param)')
conn.commit()
conn.close()

class User:
    '''
    username: nazwa użytkownika,
    password: hasło użytkownika,
    requests_count: ilość requestów wykonanych przez użytkownika
    '''
    def __init__(self, username, password, request_count):
        self.username = username
        self.password = password
        self.request_count = request_count

class Log:
    '''
    username: nazwa użytkownika k†óry wykonał zapytanie,
    date: data kiedy zapytanie zostało wykonane
    type_param: co użytkownik wybrał jako `type`,
    number_param: co użytkownik wybrał jako `number` 
    '''
    def __init__(self, username, date, type_param, number_param):
        self.username = username
        self.date = date
        self.type_param = type_param
        self.number_param = number_param


def register():
    requests_count = 0
    username = input('Wprowadź login: ')
    password = input('Wprowadż hasło: ')
    conn = sqlite3.connect('numberapp.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users VALUES (?, ?, ?)', (username, password, requests_count))
    conn.commit()
    conn.close()

def login():
    username = input('Wprowadź swój login: ')
    password = input('Wprowadż swoje hasło: ')
    conn = sqlite3.connect('numberapp.db')
    cursor = conn.cursor()
    queryset = cursor.execute('SELECT * FROM users')
    users = queryset.fetchall()
    for user in users:
            if user[0] == username:
                if user[1] == password:
                    x = user[2]
                    x += 1
                    cursor.execute('UPDATE users SET requests_count = (?) WHERE username = (?) AND password = (?)', (x, username, password))
                    conn.commit()
                    conn.close()
                    user_confirmed = User(username, password, x)
                    return user_confirmed
            conn.close()
            return False

def get_number():
    pass 

def get_logs():
    username = input('Wprowadź swój login: ')
    conn = sqlite3.connect('numberapp.db')
    cursor = conn.cursor()
    queryset = cursor.execute('SELECT * FROM logs')
    logs = queryset.fetchall()
    print(logs)

def get_users():
    conn = sqlite3.connect('numberapp.db')
    cursor = conn.cursor()
    queryset = cursor.execute('SELECT * FROM users')
    print(queryset.fetchall()) 


user = False
while True:
    if not user:
        print('1. Zarejestruj się')
        print('2. Zaloguj się')
        print('0. Wyjdź z programu')
        option = input('Podaj opcję: ')
        if option == '1':
            register()
        elif option == '2':
            user = login()
        elif option == '0':
            break
    else:
        print('1. Wykonaj zapytanie')
        print('2. Zobacz logi')
        print('3. Zobacz uzytkowników')
        print('0. Wyjdź z programu')
        option = input('Podaj opcję: ')
        if option == '1':
            get_number()
        elif option == '2':
            get_logs()
        elif option == '3':
            get_users()
        elif option == '0':
            break