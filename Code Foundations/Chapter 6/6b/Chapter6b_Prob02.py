from msilib.schema import tables
import os
os.system('cls||clear')

#----CODE STARTS HERE------

def reduce_measure(num, unit):
    cup = 0
    tablespoon = 0
    teaspoon = 0
    cup_word = 'cup' 
    tablespoon_word = 'tablespoon'
    teaspoon_word = 'teaspoon'

    if unit == 'cups' or unit == 'cup':
        cup = num
    elif unit == 'teaspoon' or unit == 'teaspoons':
        cup = num // 48
        num -= cup * 48
        tablespoon = num // 3
        num -= tablespoon * 3
        teaspoon = num
    elif unit == 'tablespoon' or unit == 'tablespoons':
        cup = num // 16
        num -= cup * 16
        tablespoon = num

    if cup > 1:
        cup_word = 'cups'
    if tablespoon > 1:
        tablespoon_word = 'tablespoons'
    if teaspoon > 1:
        teaspoon_word = 'teaspoons'
    
    if cup >= 1 and tablespoon >= 1 and teaspoon >= 1:
        return f'{cup} {cup_word}, {tablespoon} {tablespoon_word}, {teaspoon} {teaspoon_word}'
    elif cup >= 1 and tablespoon >= 1 and teaspoon == 0:
        return f'{cup} {cup_word}, {tablespoon} {tablespoon_word}'
    elif cup >= 1 and tablespoon == 0 and teaspoon >= 1:
        return f'{cup} {cup_word}, {teaspoon} {teaspoon_word}'
    elif cup == 0 and tablespoon >= 1 and teaspoon >= 1:
        return f'{tablespoon} {tablespoon_word}, {teaspoon} {teaspoon_word}'
    elif cup == 0 and tablespoon == 0 and teaspoon >= 1:
        return f'{teaspoon} {teaspoon_word}'
    elif cup >= 1 and tablespoon == 0 and teaspoon == 0:
        return f'{cup} {cup_word}'
    elif cup == 0  and tablespoon >= 1 and teaspoon == 0:
        return f'{tablespoon} {tablespoon_word}'
# One cup is equivalent to 16 tablespoons. One tablespoon is equivalent to 3 teaspoons
# 1 cup = 16 tablespoons | 1 cup = 48 teaspoons
# 1 tablespoon = 3 teaspoons

print(reduce_measure(1, 'tablespoon'))