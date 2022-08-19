import os
os.system('cls||clear')

#----CODE STARTS HERE------

centavo = int(input())
money_in_dollar = centavo / 100
print(money_in_dollar, "consists of:")

DOLLARS = int(centavo / 100)
centavo -= int(DOLLARS * 100)
print("Dollars:", DOLLARS)

QUARTERS = int(centavo / 25)
centavo -= int(QUARTERS * 25)
print("Quarters:",QUARTERS)

DIMES = int(centavo / 10)
centavo -= int(DIMES * 10)
print("Dimes:", DIMES)

NICKLES = int(centavo / 5)
centavo -= int(NICKLES * 5)
print("Nickels:", NICKLES)

PENNIES = int(centavo / 1)
centavo -= int(PENNIES * 1)
print("Pennies:", PENNIES)
