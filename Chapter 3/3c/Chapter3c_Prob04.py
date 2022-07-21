import os
os.system('cls||clear')

#----CODE STARTS HERE------
from math import pi, tan

sideLength = int(input())
numberOfSides = int(input())
polygonArea = (numberOfSides * sideLength * sideLength) / (4 * tan(pi/numberOfSides))
print(f"{polygonArea:.2f}")