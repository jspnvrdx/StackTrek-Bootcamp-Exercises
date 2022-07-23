import os
os.system('cls||clear')

#----CODE STARTS HERE------

from math import sqrt
a = float(input())
b = float(input())
c = float(input())

if a == 0 and b == 0:
    print("There is not even an unknown in this equation!")
if (b**2) - (4 * a * c) < 0:
    print("There are no solutions")

squareroot = (b**2) - (4 * a * c)

if (b**2) - (4 * a * c) > 0:
    solution1 = (-b + sqrt(squareroot)) / (2 * a)
    solution2 = (-b - sqrt(squareroot)) / (2 * a)
    print(f"There are two solutions , namely {solution1} and {solution2}")
if (b**2) - (4 * a * c) == 0:
    solution1 = (-b + sqrt(squareroot)) / (2 * a)
    print(f"There is one solution , namely {solution1}")