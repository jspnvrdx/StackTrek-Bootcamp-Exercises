import os
os.system('cls||clear')

#----CODE STARTS HERE------

month = input()
night = int(input())
month = month.title()

if month == "May" or month == "October":
    deluxe_price = 100
    premium_price = 85
elif month == "July" or month == "September":
    deluxe_price = 112.50
    premium_price = 90.58
elif month == "June" or month == "August":
    deluxe_price = 125.66
    premium_price = 100.50

deluxe_price *= night
premium_price *= night

if(month == "May" or month == "October") and (night <= 7):
    print(f"Deluxe: {deluxe_price:.2f} dollars")
    print(f"Premium: {premium_price:.2f} dollars")

elif(month == "May" or month == "October") and (night <= 14 and night > 7):
    deluxe_price -= deluxe_price * 0.05
    print(f"Deluxe: {deluxe_price:.2f} dollars")
    print(f"Premium: {premium_price:.2f} dollars")

elif(month == "May" or month == "October") and (night > 14):
    deluxe_price -= deluxe_price * 0.30
    premium_price -= premium_price * 0.10
    print(f"Deluxe: {deluxe_price:.2f} dollars")
    print(f"Premium: {premium_price:.2f} dollars")

elif(month == "July" or month == "September") and (night <= 14):
    print(f"Deluxe: {deluxe_price:.2f} dollars")
    print(f"Premium: {premium_price:.2f} dollars")

elif(month == "July" or month == "September") and (night > 14):
    deluxe_price -= deluxe_price * 0.20
    premium_price -= premium_price * 0.10
    print(f"Deluxe: {deluxe_price:.2f} dollars")
    print(f"Premium: {premium_price:.2f} dollars")

elif(month == "June" or month == "August") and (night <= 14):
    print(f"Deluxe: {deluxe_price:.2f} dollars")
    print(f"Premium: {premium_price:.2f} dollars")

elif(month == "June" or month == "August") and (night > 14):
    premium_price -= premium_price * 0.10
    print(f"Deluxe: {deluxe_price:.2f} dollars")
    print(f"Premium: {premium_price:.2f} dollars")