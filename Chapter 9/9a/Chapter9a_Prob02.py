import os
os.system('cls||clear')

#----CODE STARTS HERE------

class NumberList:
    def __init__(self, numbers, factor):
        self._numbers = numbers
        self._factor = factor

    def find_smallest_divisible(self):
        temp = -1
        try:
            for i in range(len(self._numbers)):
                if self._numbers[i] % self._factor == 0:
                    if temp == -1:
                        temp = self._numbers[i]
                    elif temp > self._numbers[i]:
                        temp = self._numbers[i]
        except:
            return -1
        return temp
            
# numbers = [1, 2, 3, 8, 0, 21, 88]
# numberList = NumberList(numbers, 3)
# numbers = [-72, 81, -36, -106, 42]
# numberList = NumberList(numbers, 7)
numbers = [1, 10, -2, -67, 4]
numberList = NumberList(numbers, 0)
print(numberList.find_smallest_divisible())