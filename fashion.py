# Fashion Class with Tax and Shipping
class Fashion:
    def __init__(self, category, brand, price):
        self.category = category
        self.brand = brand
        self.price = price

    def describe(self):
        print(f"{self.brand} {self.category} costs ${self.price}")

    def apply_discount(self, percentage):
        discount = self.price * (percentage / 100)
        self.price -= discount
        print(f"New price after {percentage}% discount: ${self.price:.2f}")

    def apply_tax(self, tax_percentage):
        tax = self.price * (tax_percentage / 100)
        self.price += tax
        print(f"Price after {tax_percentage}% tax: ${self.price:.2f}")

    def apply_shipping(self, shipping_cost):
        self.price += shipping_cost
        print(f"Price after shipping cost of ${shipping_cost}: ${self.price:.2f}")


# Test the Fashion class with tax and shipping
item1 = Fashion("Dress", "Zara", 49.99)
item1.describe()
item1.apply_discount(20)
item1.apply_tax(5)  # 5% tax
item1.apply_shipping(10)  # Shipping cost $10

item2 = Fashion("Shoes", "Nike", 89.99)
item2.describe()
item2.apply_discount(15)
item2.apply_tax(8)  # 8% tax
item2.apply_shipping(15)  # Shipping cost $15


# Polymorphism Challenge (Added Below)
class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Test polymorphism
car = Car()
plane = Plane()

car.move()   # Expected output: "Driving 🚗"
plane.move() # Expected output: "Flying ✈️"