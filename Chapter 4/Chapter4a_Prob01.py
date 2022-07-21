import os
os.system('cls||clear')

#----CODE STARTS HERE------

humanYears = int(input())

if humanYears <= 2:
    dogYears = 10.5 * (humanYears)
    print(float(dogYears))
else:
    dogYears = 21 + ((humanYears - 2) * 4)
    print(int(dogYears))