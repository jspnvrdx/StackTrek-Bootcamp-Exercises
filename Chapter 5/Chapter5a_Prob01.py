import os
os.system('cls||clear')

#----CODE STARTS HERE------

LOWER_A = ord('a')
UPPER_A = ord('A')
LOWER_Z = ord('z')
UPPER_Z = ord('Z')

message = input() 
shift = int(input()) 
new_message = ''

for i in message:
    asc = ord(i)
    new_char = asc + shift
    if (chr(asc) >='A') and (chr(asc) <= 'Z'):
        new_char = asc + shift
        if shift > 0 and new_char > UPPER_Z:
            excess = new_char - UPPER_Z
            new_char = UPPER_A + excess - 1
        elif shift < 0 and new_char < UPPER_A:
            excess = UPPER_A - shift
            new_char = UPPER_Z - excess + 1
        new_message += chr(new_char)
    elif (chr(asc) >='a') and (chr(asc) <= 'z'):
        if shift > 0 and new_char > LOWER_Z:
            excess = new_char - LOWER_Z
            new_char = LOWER_Z + excess - 1
        elif shift < 0 and new_char > LOWER_A:
            excess = LOWER_A - shift
            new_char = LOWER_A + excess - 1   
        new_message += chr(new_char)

