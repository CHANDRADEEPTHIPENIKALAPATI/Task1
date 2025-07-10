class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"Product Name: {self.name}")
        print(f"Price: ₹{self.price}")

# Creating two product objects
product1 = Product("Laptop", 55000)
product2 = Product("Smartphone", 18000)

# Displaying product details
print("Product 1:")
product1.display()

print("\nProduct 2:")
product2.display()
