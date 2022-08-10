# ---------------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("----------------------------------------------------------------------------------")
        print(key)
        print()

        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)


        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
    display_score(correct_guesses, guesses)



# ---------------------------------
def check_answer(answer, guess):
    
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
# ---------------------------------
def display_score(correct_guesses, guesses):
    print("-----------------------")
    print("RESULTS")
    print("-----------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=", ")

    print("\nGuesses: ", end="")
    for i in guesses:
        print(i, end=", ")
    
    score = int((correct_guesses / len(questions)) * 100)
    print("\nYour score is:", score, "%")

# ---------------------------------
def play_again():
    
    response = input("Do you want to play again? [Y/N]").upper()
    if response == "Y":
        return True
    else:
        return False

questions = {
    "Who developed Python Programming Language?":"C",
    "Which type of Programming does Python support?":"D",
    # "Is Python case sensitive when dealing with identifiers?":"A",
    # "Which of the following is the correct extension of the Python file?":"C",
    # "Is Python code compiled or interpreted?":"B",
    # "All keywords in Python are in _________":"D",
    # "What will be the value of the following Python expression?\n 4 + 3 % 5":"A",
    # "Which of the following is used to define a block of code in Python language?":"A",
    # "Which keyword is used for function in Python language?":"B",
    # "Which of the following character is used to give single-line comments in Python?":"B",
    # """What will be the output of the following Python code?
    
    #             i = 1
    #         while True:
    #             if i%3 == 0:
    #                 break
    #             print(i)
            
    #             i + = 1""":"B",
    # "Which of the following functions can help us to find the version of python that we are currently working on?":"A",
    # "Python supports the creation of anonymous functions at runtime, using a construct called __________":"C",
    # "What is the order of precedence in python?":"D",
    # "What will be the output of the following Python code snippet if x=1?\n x<<2":"A",
    # "What does pip stand for python?":"C",
    # "Which of the following is true for variable names in Python?":"B",
    # """What are the values of the following Python expressions?
            
    #         2**(3**2)
    #         (2**3)**2
    #         2**3**2""":"A",
    # "Which of the following is the truncation division operator in Python?":"B",
    # """What will be the output of the following Python code?
        
    #     l=[1, 0, 2, 0, 'hello', '', []]
    #     list(filter(bool, l))""":"C"
}

options = [
    ["A. Wick van Rossum", "B. Rasmus Lerdorf", "C. Guido van Rossum","D. Niene Stom"],
    ["A. object-oriented programming", "B. structured programming", "C. functional programming","D. all of the mentioned"],
#     ["A. no", "B. yes", "C. machine dependent","D. none of the mentioned"],
#     ["A. .python", "B. .pl", "C. .py","D. .p"],
#     ["A. Python code is neither compiled nor interpreted", "B. Python code is neither compiled nor interpreted", "C. Python code is only compiled","D. Python code is only interpreted"],
#     ["A. Capitalized", "B. lower case", "C. UPPER CASE","D. None of the mentioned"],
#     ["A. 7", "B. 2", "C. 4","D. 1"],
#     ["A. Indentation", "B. Key", "C. Brackets","D. All of the mentioned"],
#     ["A. Function", "B. Def", "C. Fun","D. Define"],
#     ["A. //", "B. #", "C. !","D. /*"],
#     ["A. 1 2 3", "B. error", "C. 1 2","D. none of the mentioned"],
#     ["A. sys.version(1)", "B. sys.version(0)", "C. sys.version()","D. sys.version"],
#     ["A. pi", "B. anonymous", "C. lambda","D. none of the mentioned"],
#     ["A. Exponential, Parentheses, Multiplication, Division, Addition, Subtraction", "B. Exponential, Parentheses, Division, Multiplication, Addition, Subtraction", "C. Parentheses, Exponential, Multiplication, Division, Subtraction, Addition","D. Parentheses, Exponential, Multiplication, Division, Addition, Subtraction"],
#     ["A. 4", "B. 2", "C. 1","D. 8"],
#     ["A. unlimited length", "B. all private members must have leading and trailing underscores", "C. Preferred Installer Program","D. none of the mentioned"],
#     ["A. underscore and ampersand are the only two special characters allowed", "B. unlimited length", "C. all private members must have leading and trailing underscores","D. none of the mentioned"],
#     ["A. 512, 64, 512", "B. 512, 512, 512", "C. 64, 512, 64","D. 64, 64, 64"],
#     ["A. |", "B. //", "C. /","D. %"],
#     ["A. [1, 0, 2, \'hello\', ”, []]", "B. Error", "C. [1, 2, \'hello\']","D. [1, 0, 2, 0, \'hello\', ”, []]"]
]

new_game()

while play_again():
    new_game()