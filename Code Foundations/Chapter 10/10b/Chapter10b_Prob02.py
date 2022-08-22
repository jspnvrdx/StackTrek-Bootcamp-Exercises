import os
os.system('cls||clear')

#----CODE STARTS HERE------

import heapq

class MassTesting:
    def __init__(self):
        self.data = list()
        heapq.heapify(self.data)

    def addPerson(self, person):
        return heapq.heappush(self.data, person)

    def dequeue(self):
        return heapq.heappop(self.data)


class Person:
    def __init__(self, name, age, is_hospitalized, is_healthcare_worker, with_symptoms):
        self.name = name
        self.age = age
        self.is_hospitalized = is_hospitalized
        self.is_healthcare_worker = is_healthcare_worker
        self.with_symptoms = with_symptoms

    def priority_sub_group(self):
        if self.is_hospitalized or (self.is_healthcare_worker and self.with_symptoms):
            return 1
        elif self.age >= 60:
            return 2
        elif self.is_healthcare_worker:
            return 3
        return 4

    def __lt__(self, other):
        return self.priority_sub_group() < other.priority_sub_group()

    def __repr__(self):
        return self.name

mass_testing = MassTesting()
person1 = Person("Maria", 24, False, False, False)
person2 = Person("June", 61, False, False, True)
person3 = Person("Mark", 34, True, False, True)
person4 = Person("Trish", 31, False, True, True)

mass_testing.addPerson(person1)
mass_testing.addPerson(person2)
mass_testing.addPerson(person3)
print(mass_testing.dequeue())
print(mass_testing.addPerson(person4))