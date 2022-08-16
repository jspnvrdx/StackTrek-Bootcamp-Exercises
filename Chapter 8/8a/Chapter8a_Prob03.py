import os
os.system('cls||clear')

#----CODE STARTS HERE------

class Car:

    def __init__(self, brand_name, kilometers, liters):
        self._brand_name = brand_name
        self._miles = kilometers * 1.609344
        self._uk_gal = liters * 4.54609

    def calculate_mpg(self):
        mpg = self._miles / self._uk_gal
        return float(format(mpg, '.2f'))

    def calculate_rate_of_gas(self, price):
        rog = price / self.calculate_mpg()
        return float(format(rog, '.2f'))

car = Car("BMW I8 Roadster", 40, 1.5)
print(car.calculate_mpg())
print(car.calculate_rate_of_gas(250))
