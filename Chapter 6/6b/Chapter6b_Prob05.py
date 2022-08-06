import os
os.system('cls||clear')

#----CODE STARTS HERE------

def commoncharacters( w1, w2 ):
    commonchars = []
    for i in w1:
        if i in w2:
            if i not in commonchars:
                commonchars.append(i)
    if len(commonchars) == 1:
        return 'The words have one character in common'
    return f'The words have {len(commonchars)} characters in common'
    
def check(num):
    pass

