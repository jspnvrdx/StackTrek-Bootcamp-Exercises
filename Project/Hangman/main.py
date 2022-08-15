import os
import random
from words import words
from ascii_art_hangman import eight_stages, six_stages, four_stages
from threading import Timer
os.system('cls||clear')

#----CODE STARTS HERE------

# ----------------------------------

def select_difficulty(number_of_stages, maxLives, difficulty):
    difficulty = input('Enter difficulty (EASY = 1, NORMAL = 2, HARD = 3): ')

    if difficulty == '1':
        maxLives = 8
        number_of_stages = eight_stages
    elif difficulty == '2':
        maxLives = 6
        number_of_stages = six_stages
    elif difficulty == '3':
        maxLives = 4
        number_of_stages = four_stages
    else:
        os.system('cls||clear')
        print('Please enter valid input (1-3)')
    return number_of_stages, maxLives, difficulty

# -----------------------------------

def get_word():
    word = random.choice(words).upper()
    while '-' in word or ' ' in word:
        word = random.choice(words).upper()
    return word

# -------------------------------------------------------------------------

def hangman(maxLives, stages, word, difficulty, message, used_letters):
    os.system('cls||clear')

    if not timer.is_alive():
        print('TOO BAD, YOU RAN OUT OF TIME')
        print(f'THE WORD WAS \'{word}\'')
        return

    if difficulty == '1':
        print('Dificulty: EASY')
    elif difficulty == '2':
        print('Dificulty: NORMAL')
    elif difficulty == '3':
        print('Dificulty: HARD')
    
    print(stages[maxLives])

    word_list = [letter if letter in used_letters else '-' for letter in word]
    if maxLives > 1: 
        print('Lives left:', maxLives)
    elif maxLives == 1:
        print('Life left:', maxLives)
    else:
        os.system('cls||clear')
        print('SORRY YOU RAN OUT OF LIVES, MAYBE NEXT TIME.')
        print(f'THE WORD WAS \'{word}\'')
        used_letters = list()
        return

    if word == ''.join(word_list):
        os.system('cls||clear')
        print('CONGRATULATIONS! YOU GUESSED THE WORD!')
        print(f'THE WORD WAS \'{word}\'')
        used_letters = list()
        return
    
    print(word)
    print('Used Letters:',' '.join(used_letters))
    print(message)
    print('Word:',' '.join(word_list))

    guess = input('Guess a letter: ').upper()

    if len(guess) == 1 and guess.isalpha():
        if guess in used_letters:
            message = 'You already guessed the letter'
        elif guess not in word:
            maxLives -= 1
            message = f'\'{guess}\'is not in the word'
            used_letters.append(guess)
        else:
            message = f'Good job!, \'{guess}\' is in the word'
            used_letters.append(guess)
    else:
        message = 'Please enter valid input (One letter only)'
    return hangman(maxLives, stages, word, difficulty, message, used_letters)

# -------------------------------------------------------------------------
def play_again():
    
    response = input('Do you want to play again? [Y/N]: ').upper()
    if response == 'Y':
        return True
    elif response == 'N':
        return False
    else:
        os.system('cls')
        print('Invalid choice. Please try again')
        return play_again()

# -------------------------------------------------------------------------
def timer_print(message):
    print(message)

# -------------------------------------------------------------------------

def intro(stages, maxLives, difficulty, message, word):
    stages, maxLives, difficulty, message = [], 0, '', ''
    word = get_word()
    while maxLives == 0:
        stages, maxLives, difficulty = select_difficulty(stages, maxLives, difficulty)
    return (stages, maxLives, difficulty, message, word)

def start_game():
    global stages, maxLives, difficulty, message, word, timer
    stages, maxLives, difficulty, message, word = intro(stages, maxLives, difficulty, message, word)
    timer.start()
    hangman(maxLives, stages, word, difficulty, message, used_letters=list())
    while play_again():
        timer = Timer(30,timer_print, args=('TIME\'S UP!',))
        stages, maxLives, difficulty, message, word = intro(stages, maxLives, difficulty, message, word)
        timer.start()
        hangman(maxLives, stages, word, difficulty, message, used_letters=list())

timer = Timer(30,timer_print, args=('TIME\'S UP!',))

# Global Variables
stages, maxLives, difficulty, message, word = [], 0, '', '', ''
start_game()