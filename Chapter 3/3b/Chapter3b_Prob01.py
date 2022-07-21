import os
os.system('cls||clear')

#----CODE STARTS HERE------

clock = 14.00
setAlarm = 535

clock += setAlarm
clock %= 24

print(f"{clock:.2f}")