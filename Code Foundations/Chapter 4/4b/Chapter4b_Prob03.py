import os
os.system('cls||clear')

#----CODE STARTS HERE------

call = float(input())
text = float(input())

excess_calls = float(call - 60)
excess_texts = float(text - 100)

print(f"Call minutes: {call:.1f}")
print(f"Text messages: {text:.1f}")

if excess_calls > 0:
    excess_calls *= 6.50
    print(f"Excess minute charges: {excess_calls:.2f}")
else:
    excess_calls = 0
    print(f"Excess minute charges: {excess_calls:.2f}")

if excess_texts > 0:
    print(f"Excess SMS charges: {excess_texts:.2f}")
else:
    excess_texts = 0
    print(f"Excess SMS charges: {excess_texts:.2f}")

fee_911 = 25.0
print(f"911 fee: {fee_911:.2f}")

subtotal = float(799 + fee_911 + excess_calls + excess_texts)
taxes = float(subtotal * 0.05)
print(f"Tax: {taxes:.2f}")

total_bill = taxes + subtotal
print(f"Total bill: {total_bill:.2f}")
