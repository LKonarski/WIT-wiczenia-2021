#zad1
'''def convert_string_to_number():
    x = input('Wprowadź stringa: ')
    print(int(x))

convert_string_to_number()
'''
#zad2
'''def find_min():
    lista_liczb = [34, 21, 90, 14]
    print(min(lista_liczb))

find_min()    
'''
#zad3
'''def print_list():
    for i in range(1,6):
      print(i)

print_list()      
'''
#zad4
'''def print_dict():
    x = {'a' : 1, 'b' : 2, 'c' : 3}
    for key, value in x.items():
        print(key, value)

print_dict()  
'''
#zad5
'''def get_length():
    x = input('Wprowadź dowolny wyraz: ')
    print(len(x))

get_length()
'''
#zad6
'''def remove_outer_characters():
    x = input('Wprowadź dowolny wyraz: ')
    print(x[1:-1])

remove_outer_characters()
'''
#zad7
'''def count_chars():
    x = {}
    slowo = 'przyklad'

    for tekst in slowo:
        x.update({tekst: 1})
    return x

print(count_chars())
'''