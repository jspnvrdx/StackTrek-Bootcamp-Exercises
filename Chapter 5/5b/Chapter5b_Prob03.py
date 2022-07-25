import os
os.system('cls||clear')

#----CODE STARTS HERE------

num = int(input())
factorial = 1

while num > 0:
    factorial *= num
    num -= 1
print(factorial)
