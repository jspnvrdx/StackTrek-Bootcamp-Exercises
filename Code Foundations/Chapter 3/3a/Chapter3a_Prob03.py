import os
os.system('cls||clear')

#----CODE STARTS HERE------

principal = float(input())
rate = float(input())
rate /= 100
years = float(input())

output = principal * ((1 + rate)**years)

print("{:.2f}".format(output))