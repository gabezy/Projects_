def game():
    from random import randint
    pc_wins = 0
    user_wins = 0
    while True:
        user = input('Choose one: \n[R] Rock\n[P] Paper\n[S] Scissor\n[E] Quit\n').lower()
        while user not in 'rpse':
            print('Please, Select one of the options')
            user = input('Choose one: \n[R] Rock\n[P] Paper\n[S] Scissor\n[E] Quit \n').lower()
        if user == 'e':
            print(f'Player Wins{user_wins} X Computer wins {pc_wins}')
            break
        pc = converter(randint(1, 3))
        if user == 's' and pc == 'p':
            user_wins += 1
            print(f'Player wins.\nPlayer choose {show_pick(user)} and Computer choose {show_pick(pc)}')
        elif user == 'p' and pc == 'r':
            user_wins += 1
            print(f'Player wins.\nPlayer choose {show_pick(user)} and computer choose {show_pick(pc)}')
        elif user == 'r' and pc == 's':
            user_wins += 1
            print(f'Player wins.\nPlayer choose {show_pick(user)} and Computer choose {show_pick(pc)}')
        elif user == pc:
            print(f'Tie, both choose {show_pick(pc)}')
        else:
            pc_wins += 1
            print(f'Pc wins.\nPlayer choose {show_pick(user)} and Computer choose {show_pick(pc)}')
    


def show_pick(pick):
    d1 = {'r': 'ROCK', 's': 'SCISSOR', 'p': 'PAPER'}
    if pick == 'r':
        return d1['r']
    elif pick == 's':
        return d1['s']
    return d1['p']
            


def converter(num):
    if num == 1:
        return 'r'
    elif num == 2:
        return 'p'
    else:
        return 's'

game()