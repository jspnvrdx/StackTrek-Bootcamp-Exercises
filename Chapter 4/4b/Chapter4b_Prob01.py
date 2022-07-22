import os
os.system('cls||clear')

#----CODE STARTS HERE------

time1 = int(input())
time2 = int(input())
time3 = int(input())

if (time1 > 50 and time1 < 1) and (time2 > 50 and time2 < 1) and (time3 > 50 and time3 < 1):
    print("Please enter numbers between 1 and 50")
else:
    sec = time1 + time2 + time3
    min = sec // 60
    sec -= (min * 60)

    print(f"{min}:{sec:02d}")