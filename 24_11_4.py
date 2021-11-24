def check_str_len():
    string = input("Podaj string: ")
    if len(string) > 8:
        print('OK')
    else:
        raise ValueError('Podany string jest za krótki')

check_str_len()