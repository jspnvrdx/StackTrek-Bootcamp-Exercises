import os
os.system('cls||clear')

#----CODE STARTS HERE------

def taxi(distance):
    if distance < 140:
        return "{:.2f}".format(4)
    else:
        return "{:.2f}".format((distance / 140) * 0.25 + 4)

print(taxi(7))