from abc import ABC, abstractmethod

# ============================
# ABSTRACT CLASS (Abstraction)
# ============================
class Vehicle(ABC):
    def __init__(self, name, price):
        self.name = name
        self.__price = price        # Private → Encapsulation
        self.__available = True     # Private → Encapsulation

    # Getter (Encapsulation - Controlled Access)
    def get_price(self):
        return self.__price

    # Setter (Encapsulation)
    def set_availability(self, status):
        self.__available = status

    # Check availability
    def is_available(self):
        return self.__available

    @abstractmethod
    def rent(self):  # Polymorphism
        pass


# ============================
# INHERITANCE + POLYMORPHISM
# ============================
class Car(Vehicle):
    def rent(self):  # Polymorphism
        if self.is_available():
            self.set_availability(False)
            return f"Car '{self.name}' rented for Rs.{self.get_price()}"
        return f"Car '{self.name}' is not available!"


class Bike(Vehicle):
    def rent(self):  # Polymorphism
        if self.is_available():
            self.set_availability(False)
            return f"Bike '{self.name}' rented for Rs.{self.get_price()}"
        return f"Bike '{self.name}' is already rented!"


class Truck(Vehicle):
    def rent(self):  # Polymorphism
        if self.is_available():
            self.set_availability(False)
            return f"Truck '{self.name}' rented for Rs.{self.get_price()}"
        return f"Truck '{self.name}' is unavailable!"


# ============================
# RENTAL SYSTEM  (Managing Vehicles)
# ============================
class RentalSystem:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):  # Composition
        self.vehicles.append(vehicle)

    def show_available(self):
        print("\nAvailable Vehicles:")
        for v in self.vehicles:
            if v.is_available():
                print(f"- {v.name}  →  Rs.{v.get_price()}")
        print()

    def rent_vehicle(self, name):
        for v in self.vehicles:
            if v.name.lower() == name.lower():
                print(v.rent())
                return
        print("Vehicle not found!")


# ============================
# DEMO / TESTING
# ============================
system = RentalSystem()

# Add Vehicles
system.add_vehicle(Car("Toyota Corolla", 2000))
system.add_vehicle(Bike("Yamaha R15", 500))
system.add_vehicle(Truck("Hyundai Loader", 3500))

# Show Available Vehicles
system.show_available()

# Rent Vehicles
system.rent_vehicle("Toyota Corolla")
system.rent_vehicle("Yamaha R15")
system.rent_vehicle("Yamaha R15")    # Try again (should not be available)

# Check again
system.show_available()
