import os
os.system('cls||clear')

#----CODE STARTS HERE------
from math import sqrt

sideA = int(input()) ** 2
sideB = int(input()) ** 2
sideC = sqrt(sideA + sideB)

print(f"The length of the diagonal is {sideC:.3f}.")