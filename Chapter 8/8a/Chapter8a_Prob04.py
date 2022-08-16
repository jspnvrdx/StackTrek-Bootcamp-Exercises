import os
os.system('cls||clear')

#----CODE STARTS HERE------

class Hero:
    def __init__(self):
        self._name = "Duelle"
        self._max_health = 1000
        self._current_health = self._max_health
        self._attack_power = 50

    @property
    def name(self):
        return self._name

    @property
    def max_health(self):
        return self._max_health

    @property
    def current_health(self):
        return self._current_health

    @property
    def attack_power(self):
        return self._attack_power


class Monster:

    def __init__(self, name, max_health, attack_power, hero):
        self._name = name
        self._max_health = max_health
        self._attack_power = attack_power
        self._hero = hero

    def attack(self):
        if self._hero.current_health > 0:
            return hero.current_health - self._attack_power

    def defend(self):
        if self._max_health > 0:
            return self._max_health - (self._hero.attack_power * 0.1)


hero = Hero()
monster = Monster("Zombie", 40, 800, hero)
print(monster.attack())
# print(monster.defend())