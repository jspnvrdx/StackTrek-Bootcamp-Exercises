import os
os.system('cls||clear')

#----CODE STARTS HERE------

class Student:
    def __init__(self, name, gender, course):
        self._name = name
        self._gender = gender
        self._course = course

    @property
    def name(self):
        return(self._name)

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, value):
        self._course = value
        
student = Student("Jowy Atreides", "Male", "BS Engineering")
print(student.name)