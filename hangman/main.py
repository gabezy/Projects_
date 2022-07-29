from words import words
import random as rd
from rich import print
from time import sleep

def get_valid_word(lst):
    word = rd.choice(lst)
    if '-' in word or ' ' in word:
        word = rd.choice(lst)
    return word


def title_fn(msg):
    print('='*54)
    print(msg.center(54))
    print('='*54)


def line():
    print('-'*54)
    print()


def hangman():
    word = get_valid_word(words).upper()
    print(word)
    word_set = set(word)
    used_set = set()
    lives = 6
    
    title_fn('HANGMAN')

    while len(word_set) > 0 and lives > 0:
        word_list = ' '.join([l if l in used_set else '_' for l in word])
        print(f"Lives: {lives}      Letters already used -> {' '.join(used_set)}") 
        print(word_list)
        user_letter = input('Guess a letter: ').upper()
        if len(user_letter) > 1:
            print('[red]Invalid character[/red]')
            sleep(0.5)

        elif user_letter not in used_set:
            used_set.add(user_letter)
            if user_letter in word_set:
                word_set.remove(user_letter)
                sleep(0.5)
                line()
            else:
                print(f'[red]Your letter {user_letter} is not in the word[/red]')
                sleep(0.5)
                lives -= 1
                line()
        

        elif user_letter in used_set:
            print('[yellow]Character already used[/yellow]')
            sleep(0.5)
            line()

    if lives == 0:
        print(f'Sorry, you died! The word was [green]{word}[/green]')
    else:
        print(f'Congrats!! You guessed the word \'{word}\' correct')        

        






if __name__ == '__main__':
    hangman()