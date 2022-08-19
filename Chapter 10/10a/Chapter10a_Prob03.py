import os
os.system('cls||clear')

#----CODE STARTS HERE------

class MasterCheffy:
    def __init__(self):
        self.leftovers = list()

    def store_leftover(self, leftover):
        self.leftovers.append(leftover)

    def get_leftovers(self):
        return self.leftovers

    def get_ingredients(self, quantity):
        leftover = self.leftovers[:quantity]
        del self.leftovers[:quantity]
        return leftover

master_cheffy = MasterCheffy()
master_cheffy.store_leftover("rice")
master_cheffy.store_leftover("ground beef")
master_cheffy.store_leftover("pasta")
master_cheffy.store_leftover("jam")
master_cheffy.store_leftover("salsa")
print(master_cheffy.get_ingredients(4))