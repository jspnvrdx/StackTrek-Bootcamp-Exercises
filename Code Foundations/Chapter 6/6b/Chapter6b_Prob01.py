import os
os.system('cls||clear')

#----CODE STARTS HERE------

def gregoryLeibnitz(num):
    pi = 0
    divisor = 1
    for i in range (num):
        if i % 2 == 0:
            pi += 4/divisor
            divisor += 2
        else:
            pi -= 4/divisor
            divisor += 2
    return pi

gregoryLeibnitz(12)