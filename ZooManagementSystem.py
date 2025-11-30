from abc import ABC, abstractmethod

# Abstract Class (Abstraction)
class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    __health = 100  # Private field → Encapsulation

    def __init__(self, name, age, health):
        super().__init__(name, age)
        self.__health = health

    def sound(self):   # Polymorphism
        return f"{self.name} says: Woof Woof"

    # Getter & Setter → Encapsulation
    def get_health(self):
        return self.__health

    def set_health(self, value):
        self.__health = value


class Cat(Animal):
    __health = 100

    def __init__(self, name, age, health):
        super().__init__(name, age)
        self.__health = health

    def sound(self):    # Polymorphism
        return f"{self.name} says: Meow Meow"

    def get_health(self):
        return self.__health

    def set_health(self, value):
        self.__health = value



class Lion(Animal):
    __health = 100

    def __init__(self, name, age, health):
        super().__init__(name, age)
        self.__health = health

    def sound(self):
        return f"{self.name} roars: Grrrrrr!"

    def get_health(self):
        return self.__health

    def set_health(self, value):
        self.__health = value


# List of animals in Zoo ➜ Polymorphism in Action
zoo = [
    Dog("Tommy", 4, 95),
    Cat("Kitty", 2, 80),
    Lion("Simba", 5, 90)
]

# Showing sounds of all animals (Polymorphism)
for animal in zoo:
    print(animal.sound())

print("\n--- Checking Health ---")
for animal in zoo:
    print(f"{animal.name}'s Health:", animal.get_health())

# Updating health (Encapsulation)
zoo[0].set_health(85)
print("\nAfter Treatment Tommy New Health:", zoo[0].get_health())
