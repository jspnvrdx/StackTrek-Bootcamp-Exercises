import os
os.system('cls||clear')

#----CODE STARTS HERE------

def checkPassword(password):
    password = str(password)
    if len(password) >= 8:
        if password.isupper() or password.islower() or password.isnumeric():
            return False
        else:
            return True
    else:
        return False       
    
def display(password):
    if checkPassword(password) == True:
        return "That\'s a good password"
    else:
        return "That isn\'t a good password"


print(display("CHDS4all---"))
