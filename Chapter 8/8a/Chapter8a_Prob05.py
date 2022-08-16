import os
from turtle import distance
os.system('cls||clear')

#----CODE STARTS HERE------

class Package:

    def __init__(self, weight, distance):
        self._weight = weight
        self._distance = distance

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        # set the distance too
        self._distance = value
        self.shipping_fee = value
        

    @property
    def shipping_fee(self):
        return self._shipping_fee

    @shipping_fee.setter
    def shipping_fee(self, value):
        if value > 1:
            if value >= 100:
                hundred = value // 100
                self._shipping_fee = hundred * 50
                value -= hundred * 100
                self._shipping_fee += (value * 1.5)
            else: self._shipping_fee = 45
        
        else: self._shipping_fee = 0
               

    @property
    def added_shipping_tax(self):
        if self._weight > 1:
            return self._weight * 0.25
        else: return 0

    @added_shipping_tax.setter
    def added_shipping_tax(self, value):
        # insert code
        pass

    @property
    def total_shipping_fee(self):
        return round(self._shipping_fee + self.added_shipping_tax, 2)