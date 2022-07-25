import os
os.system('cls||clear')

#----CODE STARTS HERE------
age = input()
age_cost = 0


while age != 'end':
    individual = int(age)
    if (individual >= 3 and individual <= 12):
        age_cost += 14
    elif (individual >= 65):
        age_cost += 18
    else:
        age_cost += 23

    age = input()

print(f"{age_cost:.2f}")
