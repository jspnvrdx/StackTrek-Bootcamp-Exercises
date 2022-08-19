import os
os.system('cls||clear')

#----CODE STARTS HERE------

class Queue:
    def __init__(self, size):
        self.size = size
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def add(self, element):
        if len(self.data) < self.size:
            self.data.append(element)

    def remove(self):
        if len(self.data) > 0:
            return self.data.remove(self.data[0])

    def peek(self):
      	if len(self.data) > 0:
            return self.data[0]
                
    def display(self):
        return None if len(self.data) < 1 else self.data