from random import randint
from characters import alphabet


def pw_generator(size, lst):
    pw = ''
    char = character_list(lst)
    for c in range(size):
        pw += char[randint(0, len(char)-1)]
    return pw




def  character_list(lst):
    c_list = [c for c in lst]
    return c_list

def number_pw():
    while True:
        try:
            number = input('Amount of passwords to generate: ')
            number = int(number)
        except ValueError:
            print('Invalid number')
            number = input('Amount of passwords to generate: ')
        else:
            return number


def size_pw():
        while True:
            try:
                size = input('Amount of passwords to generate: ')
                size = int(size)
            except ValueError:
                print('Invalid number')
                size = input('Amount of passwords to generate: ')
            else:
                return size


if __name__ == '__main__':
    print(pw_generator(8,alphabet))