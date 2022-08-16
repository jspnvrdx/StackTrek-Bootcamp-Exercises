import os
os.system('cls||clear')

#----CODE STARTS HERE------

class Dog:
    def __init__(self, name, breed):
        self._name = name
        self._breed = breed

    def bark(self):
        return f'{self._name} is barking'

    def run(self):
        return f'{self._name} is running'

    def eat(self, food):
        return f'{self._name} is eating {food}'


    def play(self, object):
        vowel = ['a','e','i','o','u']
        if object[0] in vowel:
          return f'{self._name} is playing with an {object}'
        else:
          return f'{self._name} is playing with a {object}'
