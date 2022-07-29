from random import randint
from rich import print

def guess(x):
    random_number = randint(1, x)
    guess_number = int(input(f'Guess a number betwwen 1 and {x}\n'))
    while guess_number != random_number:
        if guess_number > random_number:
            print('[red]Sorry, guess again. Too high[/red]')
        elif guess_number < random_number:
            print('[red]Sorry, guess again. Too low[/red]')
        guess_number = int(input(f'Guess a number betwwen 1 and {x}\n'))
    print('[green]Congrats. You have guess the number[/green]')



def cp_guess():
    from getpass import getpass
    user_number = int(getpass('Enter your secret number\n'))
    pc_number = randint(1, 10000)
    guesses = 0
    while pc_number != user_number:
        guesses += 1
        pc_number = randint(1, 10000)
    print(f'The computer found your secret number {user_number} in the {guesses}° attempt')



def computer_guess(x):
    low = 1
    high = x
    anwser = 'aa'
    attempt = 0
    while anwser not in 'Cc':
        guess_number = randint(low, high)
        anwser = input(f'Is {guess_number} too high [H], too low [L] or correct [C]\n')
        if anwser in 'Hh':
            high = guess_number - 1
            attempt += 1
        elif anwser in 'Ll':
            low = guess_number + 1
            attempt += 1
    print(f'The computer found your secret number {guess_number} in the {attempt}° attempt')

cp_guess()

