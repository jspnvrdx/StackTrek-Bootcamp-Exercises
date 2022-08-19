import os
os.system('cls||clear')

#----CODE STARTS HERE------

num = int(input())
isPrime = True

for i in range(2, num):
    if num % i == 0:
        isPrime = False

if isPrime == True:
    print("Prime")
else:
    print("Not Prime")