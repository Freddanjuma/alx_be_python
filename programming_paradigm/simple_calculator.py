class SimpleCalculator:
    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the difference of a and b."""
        return a - b

    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the result of dividing a by b. Raises ValueError if dividing by zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
