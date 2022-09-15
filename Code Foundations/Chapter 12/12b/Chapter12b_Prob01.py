import os
os.system('cls||clear')

# ----CODE STARTS HERE------


class NumberFinder:
    def __init__(self, size):
        self.size = size
        self.hashTable = [None] * size

    def hash_code(self, key):
        squared_key = key ** 2
        str_key = str(squared_key)
        key_len = len(str_key)
        half_len = key_len // 2
        first_half = str_key[:half_len]
        second_half = str_key[half_len:]
        if key_len % 2 != 0: #odd number of digits
            return int(second_half[0])
        return int(f'{first_half[-1]}{second_half[0]}') 

    def add(self, number):
        index = self.hash_code(number)
        if self.hashTable[index] is None and index < self.size:
            self.hashTable[index] = number
            return index
        return self.hashTable[index]
            
finder = NumberFinder(30)
finder.add(5)