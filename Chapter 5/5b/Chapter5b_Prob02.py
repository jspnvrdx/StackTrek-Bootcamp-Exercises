import os
os.system('cls||clear')

#----CODE STARTS HERE------

val = int(input())
count = 1
average = 0
if val == 0:
    print("No entries")
else:
    average = val
    while val != 0:
        val = int(input())
        if val == 0:
            continue
        average += val
        count += 1

average /= count
print(int(average))
