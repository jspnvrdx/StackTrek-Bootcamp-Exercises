import os
os.system('cls||clear')

#----CODE STARTS HERE------

starting_base = int(input())    # M
ending_base = int(input())      # N
ending_power = int(input())     # P

for m in range(starting_base,ending_base + 1):
    for p in range(2,ending_power+1):
        if ending_power == p:
            print(f"{m**p}", end=' ')
        elif ending_power > p:
            print(f"{m**p}", end=', ')
    print()