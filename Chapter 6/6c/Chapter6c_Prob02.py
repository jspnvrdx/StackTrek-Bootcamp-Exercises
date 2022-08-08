import os
os.system('cls||clear')

#----CODE STARTS HERE------

def adjust(input, length, padding):
    
    if length == len(input):
        return input
    return adjust(padding + input, length, padding)
    

    
        
    


# def adjust(input1, length, padding):

#   if (length == len(input1)):
#     return input1
#   newPadding = padding + input1
#   return adjust(newPadding, length,padding )

print(adjust('23',2,'0'))