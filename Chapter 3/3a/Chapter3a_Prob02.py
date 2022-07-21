import os
os.system('cls||clear')

#----CODE STARTS HERE------

eggs = int(input())

i = int(eggs % 12)
eggs -= i
eggs /= 12
eggs *= 10
print(int((eggs * 7) + (i * 7)))