import os
os.system('cls||clear')

#----CODE STARTS HERE------

def jToI():
    if os.path.exists("WORDS.TXT"):
        f = open("WORDS.TXT", "r")
    else: 
        f = open("WORDS.TXT", "x")
        f = open("WORDS.TXT", "r")


    filecontent = f.read()
    new_filecontent = ""
    for i in filecontent:
        if i == "J":
            new_filecontent += "I"
        elif i == "j":
            new_filecontent += "i"
        else:
            new_filecontent += i

    return new_filecontent
    

print(jToI())