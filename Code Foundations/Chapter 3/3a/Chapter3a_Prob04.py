import os
os.system('cls||clear')

#----CODE STARTS HERE------

pay = float(input())
tax = float(pay * 0.12)
pay -= tax
em_fund = float(pay * 0.10)
pay -= em_fund

print(f"Tax: {tax:.2f}")
print(f"Emergency Fund: {em_fund:.2f}")
print(f"Accommodation: {pay:.2f}")