import os
os.system('cls||clear')

#----CODE STARTS HERE------

def occurence_of_the():
    if os.path.exists("notes.txt"):
        f = open("notes.txt", "r")
    else: 
        f = open("notes.txt", "x")
        f = open("notes.txt", "r")
    count = 0
    for l in f:
        for word in l.split():
            word = word.upper()
            if word == "THE":
                count += 1
    print(count)
    f.close()

occurence_of_the()