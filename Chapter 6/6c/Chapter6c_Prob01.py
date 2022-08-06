import os
os.system('cls||clear')

#----CODE STARTS HERE------

def calculate(a, b):
    if a == 0 :
        return b
     
    return calculate(b%a, a)

print(calculate(60,35))