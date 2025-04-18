# This code demonstrates polymorphism in Python using a base class and derived classes.
class Vehicle:
    def move(self):
        pass 

# Subclasses
class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water 🚤")

# List of vehicle objects
vehicles = [Car(), Plane(), Boat()]

# Polymorphism in action
for v in vehicles:
    v.move()
