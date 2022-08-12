import threading as th  
## Defining of a method  
def sctn():  
    print("SECTION FOR LIFE \n")  
S = th.Timer(5, sctn)  
S.start()
print("PROGRAM TERMINATION\n")
S.cancel()