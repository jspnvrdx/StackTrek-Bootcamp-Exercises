import os
os.system('cls||clear')

# ----CODE STARTS HERE------


class Rock:
    def __init__(self, color, count):
        self.color = color
        self.count = count


class RockShelf:
    def __init__(self, size):
        self.size = size
        self.hashTable = [None] * size

    def hash_code(self, key):
        code = sum(ord(char) for char in key)
        return code % len(self.hashTable)

    def insert(self, item):
        hash_index = self.hash_code(item.color.lower())
        index_data = self.hashTable[hash_index]

        if index_data is None:
            self.hashTable[hash_index] = item
            return item.count
        elif (index_data is not None) and (index_data.color.lower() == item.color.lower()):
            self.hashTable[hash_index].count += item.count
        else:
            while self.hashTable[hash_index] is not None:
                hash_index += 1
                if hash_index == len(self.hashTable):
                    hash_index = 0
            self.hashTable[hash_index] = item
        return self.hashTable[hash_index].count

    def search(self, color):
        index = 0
        for x in self.hashTable:
            if x is None:
                continue
            if x.color.lower() == color.lower():
                return x.count
        return 0

rock1 = Rock("green", 5)
rock2 = Rock("orange", 1)
rock3 = Rock("BLUE", 12)
shelf = RockShelf(10)
shelf.insert(rock1)
shelf.insert(rock2)
shelf.insert(rock3)
print(shelf.search("red"))
# rock1 = Rock("green", 5)
# rock2 = Rock("gREeN", 5)
# shelf = RockShelf(10)
# print(shelf.insert(rock1))
# print(shelf.insert(rock2))
# print(shelf.search("green"))
