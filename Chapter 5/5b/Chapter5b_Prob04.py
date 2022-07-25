import os
os.system('cls||clear')

#----CODE STARTS HERE------

flag = True
count = 0;
first_x = 0
first_y = 0
temp_x = 0
temp_y  = 0
subtotal = 0
while flag == True:
    x = input()
    if(x == 'end'):
        flag = False
        continue
    else:
        y = input()
        if count == 0:
            first_x = int(x)
            first_y = int(y)
        else:
            subtotal += temp_x * int(y) - temp_y * (x)
