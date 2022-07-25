import os
os.system('cls||clear')

#----CODE STARTS HERE------

age = int(input())
target_money = float(input())
toy_price = int(input())

money = 0
toy = 0

for i in range(0,age):
    i += 1
    if i % 2 == 0:
        money += 1
    else:
        toy += 1

bday_moneys = 0
for years in range(0,money):
    years += 1
    bday_moneys += 10 * years
    bday_moneys -= 1

total_toy_price = 0
for years in range(0,toy):
    total_toy_price += toy_price

savings = bday_moneys + total_toy_price

if savings < target_money:
    print(f"No! you still need {(target_money - savings):.2f}")
elif target_money < savings:
    print(f"Yes! you still have {savings - target_money:.2f} left")