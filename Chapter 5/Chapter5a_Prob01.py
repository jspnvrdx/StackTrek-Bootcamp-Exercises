import os
os.system('cls||clear')

#----CODE STARTS HERE------

message = input()
shift = int(input())

UPPER_A = ord('A')
UPPER_Z = ord('Z')
LOWER_A = ord('a')
LOWER_Z = ord('z')
new_message = ''

for char in message:
    asci = ord(char)
    if chr(asci) >= 'A' and chr(asci) <= 'Z':
        asci += shift
        if asci > UPPER_Z:
            excess = asci - UPPER_Z
            asci = UPPER_A + excess - 1
        elif asci < UPPER_A:
            excess = UPPER_A - asci
            asci = UPPER_Z - asci
    elif chr(asci) >= 'a' and chr(asci) <= 'z':
        asci += shift
        if asci > LOWER_Z:
            excess = asci - LOWER_Z
            asci = LOWER_A + excess - 1
        elif asci < LOWER_A:
            excess = LOWER_A - asci
            asci = UPPER_Z - asci
    new_message += chr(asci)
    
print(new_message)
