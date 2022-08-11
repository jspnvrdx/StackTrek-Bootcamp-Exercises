import os
import random
from ascii_art_hangman import eight_stages, six_stages, four_stages
from words import words
os.system('cls||clear')

#----CODE STARTS HERE------

play = True    
while play:
    # Selecting dificulties that will determine the number of lives
    number_of_stages = []
    maxLives = 0
    while maxLives == 0:
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

    # Getting random word from words.py
    word = random.choice(words).upper()
    while '-' in word or ' ' in word:
        word = random.choice(words).upper()

    # word_letter = set(word)
    used_letters = set()
    message = ''
    flag = True
    # Start of hangman game
    while flag:
        os.system('cls||clear')

        if difficulty == 1:
            print('Dificulty: EASY')
        elif difficulty == 2:
            print('Dificulty: NORMAL')
        elif difficulty == 3:
            print('Dificulty: HARD')
        
        # print ascii art for stages
        print(number_of_stages[maxLives])
        

        word_list = [letter if letter in used_letters else '-' for letter in word]
        if maxLives > 1: 
            print('Lives left:', maxLives)
        elif maxLives == 1:
            print('Life left:', maxLives)
        else:
            flag = False
            os.system('cls||clear')
            print('SORRY YOU RAN OUT OF LIVES, MAYBE NEXT TIME.')
            print(f'THE WORD WAS \'{word}\'')
            continue
            
        if word == ''.join(word_list):
            flag = False
            os.system('cls||clear')
            print('CONGRATULATIONS! YOU GUESSED THE WORD!')
            print(f'THE WORD WAS \'{word}\'')
            continue
            
        print('Used Letters:',' '.join(used_letters),'\n')
        print(message)
        print(word)
        print('Word:',' '.join(word_list))
        
        guess = input('Guess a letter: ').upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in used_letters:
                message = 'You already guessed the letter'
            elif guess not in word:
                maxLives -= 1
                message = f'\'{guess}\'is not in the word'
                used_letters.add(guess)
            else:
                message = f'Good job!, \'{guess}\' is in the word'
                used_letters.add(guess)
        else:
            message = 'Please enter valid input (One letter only)'
        
        # --------------------------------------
    playAgainPrompt = ''
    while playAgainPrompt != 'Y' and playAgainPrompt != 'N':
        playAgainPrompt = input('Play again? (Y/N) : ').upper()
        if playAgainPrompt == 'Y':
            continue 
        elif playAgainPrompt == 'N':
            play = False
            break  
        else:
            os.system('cls||clear')
            print('Please enter valid input (Y/N)')
            continue