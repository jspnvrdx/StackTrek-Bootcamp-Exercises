import os
os.system('cls||clear')

#----CODE STARTS HERE------

class Counter:
    def __init__(self, number):
        self._number = number

    def numbers_divisible_by_three(self):
        three = set()
        for num in range(1, self._number + 1):
            if num % 3 == 0:
                three.add(num)
        return three

    def odd_numbers(self):
        even = set()
        for num in range(1, self._number + 1):
            if not num % 2 == 0:
                even.add(num)
        return even

    def even_numbers(self):
        even = set()
        for num in range(1, self._number + 1):
            if num % 2 == 0:
                even.add(num)
        return even

    def even_numbers_intersection(self):
        return self.numbers_divisible_by_three().intersection(self.even_numbers())

    def odd_numbers_intersection(self):
        return self.numbers_divisible_by_three().intersection(self.odd_numbers())

counter = Counter(20)
print(counter.even_numbers())
print(counter.odd_numbers())
print(counter.even_numbers_intersection())
print(counter.odd_numbers_intersection())