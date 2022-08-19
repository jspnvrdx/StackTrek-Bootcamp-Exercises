import os
os.system('cls||clear')

#----CODE STARTS HERE------
from math import cos, radians, sin
initialVelocity = float(input()) # V0
angle = radians(float(input())) #θ
time = float(input()) #t
G = 9.81

x = initialVelocity * cos(angle) * time
y = (initialVelocity * sin(angle) * time) - (0.5 * G * (time ** 2))
print(f"{x:.0f}, {y:.0f}")