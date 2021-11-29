#zad1
'''
number = input('Wprowadź liczbę większą od 0: ')
def digitize(number):
    print(list(map(int, str(number))))

digitize(number)
'''
#zad2
'''
import random

def roll_dice():
    number = random.randint(1, 6)
    print('Liczba wylosowanych oczek to', number)

roll_dice()
'''
#zad3
'''
import random

numbers = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

def roll_dice_times(n):
    i = 0
    while i < n:
        number = random.randint(1, 6)
        if number in numbers.keys():
            numbers[number] += 1
        i += 1
    for values in numbers.values():
        if values >= 2:
            print(True)


roll_dice_times(3)
'''
#zad4
'''
import random
roll_dice_1 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
roll_dice_2 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

print('Proporcje')

def roll_two_dice_times(n):
    i = 0
    while i < n:
        number_1 = random.randint(1, 6)
        if number_1 in roll_dice_1.keys():
            roll_dice_1[number_1] += 1

        number_2 = random.randint(1, 6)
        if number_2 in roll_dice_2.keys():
            roll_dice_2[number_2] += 1
        i += 1

    x = 1
    while x <= 6:
        print(f'{x}, {roll_dice_1[x]} do {roll_dice_2[x]}')
        x += 1


roll_two_dice_times(4)
'''
#zad5
#plik wypozyczalnia.py