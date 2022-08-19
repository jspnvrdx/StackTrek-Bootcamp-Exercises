import os
os.system('cls||clear')

#----CODE STARTS HERE------

class NumberList:
    def __init__(self, numbers):
        self._numbers = numbers

    def find_values(self):
        temp = -1
        index = -1
        for i in self._numbers:
            if i % 2 == 0:
                if temp < i:
                    temp = i

        for j in range(len(self._numbers)):
            if temp == self._numbers[j]:
                index = j
                break
        if not (temp == -1 and index == -1):
            return f'{temp} at index {index}'
        return None

numbers = [36, 36, 36, 36, 36, 36, 36]
numberList = NumberList(numbers)
print(numberList.find_values())