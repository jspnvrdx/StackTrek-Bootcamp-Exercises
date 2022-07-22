import os
os.system('cls||clear')

#----CODE STARTS HERE------

month = input()
night = int(input())
deluxe_price = 100
premium_price = 85

if (month == "May" or month == "October") and (night <= 7):
    deluxe_price *= night
    deluxe_price -= deluxe_price * 0.05
    print(f"Deluxe: {deluxe_price:.2f} dollars")
    print(f"Premium: {premium_price:.2f} dollars")
if((month == "May" or month == "October") and (night <= 14 and night > 7)):
    deluxe_price *= night
    deluxe_price *= 0.30
    print(f'''Deluxe: {deluxe_price:.2f} dollars 
    Premium: {premium_price:.2f} dollars''')