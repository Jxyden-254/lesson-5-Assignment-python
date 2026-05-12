"""
Lesson 5: Object-Oriented Programming Concepts
Demonstrates Inheritance, Polymorphism, and Encapsulation
"""

from abc import ABC, abstractmethod
from typing import List


# ============================================================================
# SUPERHERO EXAMPLE - Inheritance, Polymorphism, and Encapsulation
# ============================================================================

class Superhero(ABC):
    """
    Abstract base class representing a generic superhero.
    
    Attributes:
        name (str): The superhero's name
        power (str): The superhero's primary power
        city (str): The city the superhero protects
    """
    
    def __init__(self, name: str, power: str, city: str) -> None:
        """
        Initialize a superhero with name, power, and city.
        
        Args:
            name: The superhero's name
            power: The superhero's primary power
            city: The city the superhero protects
            
        Raises:
            ValueError: If any parameter is empty or None
        """
        if not all([name, power, city]):
            raise ValueError("Name, power, and city cannot be empty")
        
        self.name = name
        self.power = power
        self.city = city
    
    def introduce(self) -> None:
        """Introduce the superhero and their city."""
        print(f"I am {self.name}, protector of {self.city}!")
    
    @abstractmethod
    def use_power(self) -> None:
        """Use the superhero's power. Must be implemented by subclasses."""
        pass
    
    def __repr__(self) -> str:
        """Return a string representation of the superhero."""
        return f"{self.__class__.__name__}(name='{self.name}', power='{self.power}', city='{self.city}')"


class FlyingHero(Superhero):
    """
    A superhero with flying abilities.
    
    Extends Superhero with flight speed capability.
    Demonstrates Polymorphism by overriding use_power()
    """
    
    def __init__(self, name: str, power: str, city: str, flight_speed: int) -> None:
        """
        Initialize a flying superhero.
        
        Args:
            name: The superhero's name
            power: The superhero's primary power
            city: The city the superhero protects
            flight_speed: Maximum flight speed in km/h
        """
        super().__init__(name, power, city)
        self.flight_speed = flight_speed
    
    def use_power(self) -> None:
        """Use the flying power to combat threats."""
        print(f"{self.name} soars through the sky at {self.flight_speed} km/h, using {self.power}!")


class TechHero(Superhero):
    """
    A tech-savvy superhero with gadgets.
    
    Demonstrates Encapsulation with private methods (__show_gadgets).
    Demonstrates Polymorphism by overriding use_power()
    """
    
    def __init__(self, name: str, power: str, city: str, gadgets: List[str]) -> None:
        """
        Initialize a tech-based superhero.
        
        Args:
            name: The superhero's name
            power: The superhero's primary power
            city: The city the superhero protects
            gadgets: List of available gadgets
        """
        super().__init__(name, power, city)
        self.gadgets = gadgets
    
    def __show_gadgets(self) -> None:
        """
        Private method to display gadgets.
        Demonstrates Encapsulation - hidden from outside access.
        """
        print("Gadgets:", ", ".join(self.gadgets))
    
    def use_power(self) -> None:
        """Use the tech power with available gadgets."""
        print(f"{self.name} activates {self.power} using high-tech gadgets!")
        self.__show_gadgets()


# ============================================================================
# VEHICLE EXAMPLE - Polymorphism in Action
# ============================================================================

class Vehicle(ABC):
    """Abstract base class representing a generic vehicle."""
    
    @abstractmethod
    def move(self) -> None:
        """Move the vehicle. Must be implemented by subclasses."""
        pass
    
    def __repr__(self) -> str:
        """Return a string representation of the vehicle."""
        return f"{self.__class__.__name__}()"


class Car(Vehicle):
    """A vehicle that drives on roads."""
    
    def move(self) -> None:
        """Drive the car."""
        print("The car is driving 🚗")


class Plane(Vehicle):
    """A vehicle that flies through the air."""
    
    def move(self) -> None:
        """Fly the plane."""
        print("The plane is flying ✈️")


class Boat(Vehicle):
    """A vehicle that sails on water."""
    
    def move(self) -> None:
        """Sail the boat."""
        print("The boat is sailing 🚤")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("SUPERHERO EXAMPLE")
    print("=" * 60)
    
    # Creating superhero objects
    hero1 = Superhero("Iron Shield", "Super Strength", "Metropolis")
    hero2 = FlyingHero("Sky Falcon", "Wind Blast", "Aero City", 800)
    hero3 = TechHero(
        "Gadgeteer",
        "Laser Beam",
        "Neo Tokyo",
        ["Jet Boots", "Laser Gauntlet", "Drone"]
    )
    
    # Testing superhero methods
    print("\nHero 1:")
    hero1.introduce()
    hero1.use_power()
    
    print("\nHero 2:")
    hero2.introduce()
    hero2.use_power()
    
    print("\nHero 3:")
    hero3.introduce()
    hero3.use_power()
    
    print("\n" + "=" * 60)
    print("VEHICLE EXAMPLE - Polymorphism in Action")
    print("=" * 60 + "\n")
    
    # Polymorphism: Same method call, different behavior
    vehicles: List[Vehicle] = [Car(), Plane(), Boat()]
    
    for vehicle in vehicles:
        vehicle.move()
