# Fashion Project

Welcome to the Fashion Project! This repository contains a Python-based program designed to manage fashion-related items like clothing and accessories. It supports features like applying discounts, taxes, shipping costs, and offers the flexibility of using object-oriented programming concepts like inheritance and polymorphism.

## Features

- **Product Description**: Define items like clothes, shoes, bags, etc., with details such as brand and price.
- **Apply Discount**: Add functionality to apply discounts based on percentages.
- **Apply Tax**: Automatically calculate and apply tax on the product.
- **Apply Shipping**: Add shipping costs to the final price of the product.
- **Inheritance**: Use inheritance to add specialized behavior to certain types of fashion items (like shoes or bags).
- **Polymorphism**: Different classes for various items that share common functionality but behave differently.

## Requirements

- Python 3.x

## Installation

To get started with this project on your local machine, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/carolinekibaara/fashion.git
    ```

2. Navigate to the project folder:

    ```bash
    cd fashion
    ```

3. Install any required dependencies (if applicable):

    ```bash
    pip install -r requirements.txt
    ```

   _Note: If no `requirements.txt` file is present, you can skip this step._

4. Run the project:

    ```bash
    python fashion.py
    ```

## Usage Example

Here’s a basic example of how the program works:

```python
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

# Example Usage
item = Fashion("Dress", "Zara", 49.99)
item.describe()
item.apply_discount(20)
item.apply_tax(5)  # 5% tax
item.apply_shipping(10)  # Shipping cost $10
