from random import choice

class Coffee:
    def __init__ (self, roast, make, addon):
        self.roast = roast
        self.make = make
        self.addon = addon

    def get_roast(self):
        return self.roast
    
    def set_roast(self, new_roast):
        self.roast = new_roast

    def get_make(self):
        return self.make
    
    #def set_make(self, new_make):
    #    self.make = new_make

    def set_make(self):
        self.make = choice(["drip", "french press", "espresso", "americano"])

my_coffee = Coffee("dark", "drip", "sugar")

#print(my_coffee.roast)
roast_level = my_coffee.get_roast()
print(roast_level)

#print(my_coffee.make)
print(my_coffee.get_make())
print(my_coffee.addon)

kerek_coffee = Coffee("dark", "americano", "none")
print(kerek_coffee.make)

#print(my_coffee)

my_coffee.set_roast("light")
roast_level = my_coffee.get_roast()
print(roast_level)

#my_coffee.set_make("espresso")
my_coffee.set_make()
print(my_coffee.get_make())