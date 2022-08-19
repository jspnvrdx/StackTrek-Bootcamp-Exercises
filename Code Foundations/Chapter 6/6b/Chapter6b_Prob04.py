import os
os.system('cls||clear')

#----CODE STARTS HERE------

def gcd(n,m):
    d = min(m,n)
    while m % d != 0 and n % d != 0:
        d -= 1
    return d

def reduce(num, den):
    g = gcd(num,den)
    if num == 0:
        return '0/1'
    else:
        num /= g
        den /= g
    return f'{num}/{den}'
def display(num, den):
    return f'{num}/{den} can be reduce to {reduce(num,den)}'

print(display(63,6))
