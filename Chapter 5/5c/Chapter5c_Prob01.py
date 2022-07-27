import os
os.system('cls||clear')

#----CODE STARTS HERE------

number = int(input())
m = 0
f = 0

for count in range(1, number+1):
    i = input()
    if i == 'm':
        m += 1
    elif i == 'f':
        f += 1
    else:
        pass

d = 0

if m < f:
    d = f
elif m > f:
    d = m
else:
    d = m

for count in range(0,d+1):
    if m % d == 0 and f % d == 0:
        break
    else:
        d -= 1
        continue

m_ratio = m // d
f_ratio = f // d

print(f"Males: {m}")
print(f"Females: {f}")
if m_ratio == 0:
    print("All females")
elif f_ratio == 0:
    print("All males")
else:
    print(f"{m_ratio}:{f_ratio}")