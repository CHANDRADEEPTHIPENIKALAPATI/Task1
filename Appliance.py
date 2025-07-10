from abc import ABC, abstractmethod

class Appliance():
    def turn_on(self):
        pass
class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing machine turn on")
class Fridge(Appliance):
    def turn_on(self):
        print("Fridge turn on")
w=WashingMachine()
f=Fridge()
w.turn_on()
f.turn_on()
