import os
os.system('cls||clear')

#----CODE STARTS HERE------

class BiscuitBox: 
	
    def __init__(self, biscuits): 
        self._biscuits = biscuits
    
    def get_biscuit_type(self): 
        for i in range(len(self._biscuits)):
            temp = self._biscuits[i]
            for j in range(i+1,len(self._biscuits)):
                if temp.upper() == self._biscuits[j].upper():
                    return temp
        return 'None'

# biscuits =  ["rich tea", "marie", "pop Tarts", "oates", "plain", "plain"]
biscuits =  ["marie", "pop Tarts", "oates", "PLAin", "pLain"]
box = BiscuitBox(biscuits)
print(box.get_biscuit_type())