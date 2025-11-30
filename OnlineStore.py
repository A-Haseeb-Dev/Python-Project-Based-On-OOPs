from abc import ABC, abstractmethod

# Abstract Class — Abstraction
class Product(ABC):
    def __init__(self, name, price, stock):
        self.name = name
        self.__price = price   # Encapsulation
        self.__stock = stock   # Encapsulation

    # Abstract method — Polymorphism
    @abstractmethod
    def calculateDiscount(self):
        pass

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def reduce_stock(self, qty):
        if qty <= self.__stock:
            self.__stock -= qty
            return True
        return False


class Electronics(Product):
    def __init__(self, name, price, stock, warranty):
        super().__init__(name, price, stock)
        self.warranty = warranty

    def calculateDiscount(self):   # Polymorphism
        return self.get_price() * 0.10   # 10% discount


class Clothes(Product):
    def __init__(self, name, price, stock, size):
        super().__init__(name, price, stock)
        self.size = size

    def calculateDiscount(self):   # Polymorphism
        return self.get_price() * 0.20   # 20% discount


class Cart:
    def __init__(self):
        self.items = []  # list of tuples (product, quantity)

    def add_item(self, product, qty):
        if product.reduce_stock(qty):
            self.items.append((product, qty))
            print(f"Added {qty} of {product.name} to cart.")
        else:
            print(f"Not enough stock for {product.name}")

    def calculate_total(self):
        total = 0
        for product, qty in self.items:
            price = product.get_price()
            discount = product.calculateDiscount()
            total += (price - discount) * qty
        return total


# Products
laptop = Electronics("HP Laptop", 80000, 5, "2 years")
tshirt = Clothes("Black T-Shirt", 2000, 10, "Medium")

# Cart
cart = Cart()
cart.add_item(laptop, 1)
cart.add_item(tshirt, 2)

# Total Bill
total = cart.calculate_total()
print("\nFinal Bill:", total)
