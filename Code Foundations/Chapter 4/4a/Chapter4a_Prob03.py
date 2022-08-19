import os
os.system('cls||clear')

#----CODE STARTS HERE------

month = int(input())

if month == 2:
    print("28 or 29 days")
elif (month % 2 == 0 and month <= 6) or (month % 2 == 1 and month > 7):
    print("30 days")
elif (month % 2 == 1 and month <= 7) or (month % 2 == 0 and month > 6):
    print("31 days")
else:
    print("Invalid! Please try again")