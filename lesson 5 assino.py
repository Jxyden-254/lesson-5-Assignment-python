# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city
    
    def introduce(self):
        print(f"I am {self.name}, protector of {self.city}!")
    
    def use_power(self):
        print(f"{self.name} uses {self.power}!")

# Subclass (Inheritance)
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed
    
    # Polymorphism — overriding use_power()
    def use_power(self):
        print(f"{self.name} soars through the sky at {self.flight_speed} km/h, using {self.power}!")

# Another subclass
class TechHero(Superhero):
    def __init__(self, name, power, city, gadgets):
        super().__init__(name, power, city)
        self.gadgets = gadgets
    
    # Encapsulation example
    def __show_gadgets(self):
        print("Gadgets:", ", ".join(self.gadgets))
    
    def use_power(self):
        print(f"{self.name} activates {self.power} using high-tech gadgets!")
        self.__show_gadgets()

# Creating objects
hero1 = Superhero("Iron Shield", "Super Strength", "Metropolis")
hero2 = FlyingHero("Sky Falcon", "Wind Blast", "Aero City", 800)
hero3 = TechHero("Gadgeteer", "Laser Beam", "Neo Tokyo", ["Jet Boots", "Laser Gauntlet", "Drone"])

# Testing methods
hero1.introduce()
hero1.use_power()

hero2.introduce()
hero2.use_power()

hero3.introduce()
hero3.use_power()
class Vehicle:
    def move(self):
        print("The vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print("The car is driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("The plane is flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("The boat is sailing 🚤")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
