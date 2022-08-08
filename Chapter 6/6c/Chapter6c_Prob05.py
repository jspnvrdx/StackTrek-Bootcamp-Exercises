import os
os.system('cls||clear')

#----CODE STARTS HERE------

def calculate(numbers, digits):
    return f'1 in {factorial(numbers) / (factorial(digits) * factorial(numbers-digits)):.0f}'


def factorial(number):
    if number == 1:
        return number
    return number*factorial(number-1)

print(calculate(61, 7))