
import os
os.system('cls||clear')

#----CODE STARTS HERE------
from math import sqrt
distance = int(input()) #d
acceleration = float(9.8) # a
initialVelocity = float(0) # Vi
finalVelocity = (initialVelocity ** 2) + (2 * acceleration * distance) #Vf
finalVelocity = sqrt(finalVelocity)
print(f"{finalVelocity:.2f}")