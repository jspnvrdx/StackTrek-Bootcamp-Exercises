import os
os.system('cls||clear')

#----CODE STARTS HERE------

def multiplex(n):
    #solution here
    var = ""
    while n:
        var += printx(n)
        n -= 1
    return var

def printx(n):
    #solution here
    return "x"

multiplex(5)