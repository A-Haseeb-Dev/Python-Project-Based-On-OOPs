from abc import ABC, abstractmethod

# Abstract class – Abstraction
class Item(ABC):
    def __init__(self, title, price):
        self.title = title
        self.price = price

    @abstractmethod
    def checkout(self):
        pass



class Book(Item):
    __available = True   # Private field → Encapsulation

    def __init__(self, title, author, price):
        super().__init__(title, price)
        self.author = author

    def checkout(self):   # Polymorphism
        if self.__available:
            self.__available = False
            return f"Book '{self.title}' issued successfully."
        else:
            return f"Book '{self.title}' is already issued."

    def get_availability(self):
        return self.__available

    def return_item(self):
        self.__available = True


class Magazine(Item):
    __copies_left = 3    # Encapsulation (private field)

    def __init__(self, title, issue_no, price):
        super().__init__(title, price)
        self.issue_no = issue_no

    def checkout(self):   # Polymorphism
        if self.__copies_left > 0:
            self.__copies_left -= 1
            return f"Magazine '{self.title}' (Issue {self.issue_no}) issued."
        else:
            return f"No copies left for '{self.title}'."

    def get_copies(self):
        return self.__copies_left

    def add_copies(self, count):
        self.__copies_left += count



class Member:
    __fine = 0   # Private field → Encapsulation

    def __init__(self, name):
        self.name = name

    def add_fine(self, amount):
        self.__fine += amount

    def get_fine(self):
        return self.__fine

    def pay_fine(self, amount):
        if amount <= self.__fine:
            self.__fine -= amount
            return f"{self.name} paid fine of {amount}. Remaining: {self.__fine}"
        return f"Amount is greater than fine!"



# Create Library Items
items = [
    Book("Atomic Habits", "James Clear", 500),
    Book("Rich Dad Poor Dad", "Robert Kiyosaki", 450),
    Magazine("Tech Today", 15, 150)
]

# Create Members
member1 = Member("Ali")

# Checkout items
for item in items:
    print(item.checkout())

print("\n--- Availability Check ---")
for item in items:
    if isinstance(item, Book):
        print(f"{item.title} Available:", item.get_availability())
    elif isinstance(item, Magazine):
        print(f"{item.title} Copies Left:", item.get_copies())

# Fine Example
member1.add_fine(100)
print("\nFine on Member:", member1.get_fine())
print(member1.pay_fine(50))
print("Remaining Fine:", member1.get_fine())
