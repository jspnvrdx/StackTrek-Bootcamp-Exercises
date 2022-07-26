import os
os.system('cls||clear')

#----CODE STARTS HERE------
# "kitten" and "sitting"
def editDistance(s,t):
    if len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    else:
        cost = 0
    
    if s[len(s)-1] != t[len(t)-1]:
        cost = 1
    
    d1 = editDistance(s[:-1],t) + 1
    d2 = editDistance(s,t[:-1]) + 1
    d3 = editDistance(s[:-1],t[:-1]) + cost

    return min(d1,d2,d3)
def display(s,t):
    return f'The edit distance between {s} and {t} is {editDistance(s,t)}'

print(display('kitten','sitting'))
print(display('cake', 'bake'))