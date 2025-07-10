class Calculator:
    #addition of two numbers
    def add(self, a, b):
        return a + b
    #subtraction of two numbers
    def subtract(self, a, b):
        return a - b
    #multiplication of two numbers
    def multiply(self, a, b):
        return a * b
    #division of two numbers
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b

# Create an instance of Calculator
c= Calculator()

# Perform calculations
print("Addition (10 + 5):", c.add(10, 5))
print("Subtraction (10 - 5):", c.subtract(10, 5))
print("Multiplication (10 * 5):", c.multiply(10, 5))
print("Division (10 / 5):", c.divide(10, 5))
print("Division (10 / 0):", c.divide(10, 0))