import os
import random
from words import words
from ascii_art_hangman import eight_stages, six_stages, four_stages
os.system('cls||clear')

#----CODE STARTS HERE------

def game_timer():
    pass
# ----------------------------------
def select_difficulty(number_of_stages, maxLives):
    pass
# -----------------------------------
def get_word():
    word = random.choice(words).upper()
    while '-' in word or ' ' in word:
        word = random.choice(words).upper()
    return word

    
# -----------------------------------
def start_game():
    pass


start_game()