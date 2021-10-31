#zad1
'''lista = [1,2,3,4,5]
odwrocona_lista = lista[::-1]
print('odwrocona_lista = ' + str(odwrocona_lista))'''

#zad2
'''lista = [1,2,3,4,5]
val1_max = max(lista)
lista.remove(val1_max)
val2_max = max(lista)
lista_max = [val1_max, val2_max]

print('lista_max =  ' + str(lista_max))'''

#zad3
'''lista = []
for i in range(3,14):
    lista.append(i)
print('lista1 = ' + str(lista))

x = 0
lista2 = []
while(x <= 10):
    lista2.append(x)
    x = x + 1
    
print('lista2 = ' + str(lista2))'''
    
#zad4
'''while True:
    dane_logowania = {'Admin' : '1234'}
    login = input('Wprowadź nazwę użytkownika: ')
    haslo = input('Wprowadź hasło: ')
    
    if dane_logowania.get(login) and haslo == dane_logowania.get(login):
        print('Logowanie poprawne')
        break
    else:
        print('Logowanie nieudane, wprowadź dane ponownie')'''


#zad5
'''lista1 = [1,2,3,4,5]
lista2 = [1,2,3,4,5]
lista3 = [1,2,2,3,3,4,5]

x = set(lista1 and lista2 and lista3)
print(x)

if len(set(lista1)) !=  len(set(lista2)) or len(set(lista3)):
    print('Wszystkie listy zawierają te same elementy, lista3 zawiera duplikaty')
else:
    print ('Wszystkie listy zawierają te same elementy, lista3 nie zawiera duplikatów')'''

 
