import os
os.system('cls||clear')

#----CODE STARTS HERE------

def median(a,b,c):
  if a > b:
    if a < c:
      return a
    elif b > c:
      return b
    else:
      return c
  else:
    if a > c:
      return a
    elif b < c:
      return b
    else:
      return c

def alternate_median(a,b,c):
  return median(a,b,c) + 2

def printx(a,b,c):
   return f"The median value is {median(a,b,c)} and the value for the alternate median function is {alternate_median(a,b,c)}"