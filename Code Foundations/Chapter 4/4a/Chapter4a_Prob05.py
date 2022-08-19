import os
os.system('cls||clear')

#----CODE STARTS HERE------

targetDonation = int(input()) 
puzzles = int(input()) 
talkingDolls = int(input()) 
teddyBear = int(input()) 
pokemonPlushies = int(input()) 
bigToyTruck = int(input()) 

total_amount = (puzzles * 14) + (talkingDolls * 3) + (teddyBear * 20.2) + (pokemonPlushies * 8.20) + (bigToyTruck * 10.65)
total = puzzles + talkingDolls + teddyBear + pokemonPlushies + bigToyTruck

if total >= 50:
    total_amount -= (total_amount * 0.25)
    
total_amount -= (total_amount * 0.1)
total_amount -= targetDonation

if total_amount >= 0:
    print(f"Yes! {total_amount:.2f} dollars left.")
else:
    print(f"Not enough money! {-total_amount:.2f} dollars needed.")