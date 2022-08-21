import os
os.system('cls||clear')

#----CODE STARTS HERE------

import heapq


class Airport:
    def __init__(self):
        self.data = list()
        heapq.heapify(self.data)

    def add_passenger(self, passenger):
        heapq.heappush(self.data, (passenger.is_pregnant, passenger.with_children))

    def dequeue(self):
        return heapq.heappop(self.data)


class Passenger:
    def __init__(self, name, age, is_pregnant, with_children):
        self.name = name
        self.age = age
        self.is_pregnant = is_pregnant
        self.with_children = with_children
        

    def sub_group(self):
        # insert code
        pass

    def __repr__(self):
        # insert code
        pass

    def __lt__(self, other):
        return other < 60

airport = Airport()
passenger1 = Passenger("Henry", 27, False, False)
passenger2 = Passenger("Jen", 25, True, False)
passenger3 = Passenger("Nica", 67, False, False)

airport.add_passenger(passenger1)
airport.add_passenger(passenger2)
airport.add_passenger(passenger3)
print(airport.dequeue())