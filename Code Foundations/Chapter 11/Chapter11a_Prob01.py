import os
os.system('cls||clear')

#----CODE STARTS HERE------

def sort(elements):
    for i in range(1,len(elements)):
        j = i-1
        nxt = elements[i]
        while(elements[j] > nxt) and (j >= 0):
            elements[j+1] = elements[j]
            j = j-1
        elements[j+1] = nxt
    return elements

