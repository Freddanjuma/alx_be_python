class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

    @classmethod
    def description(cls):
        return "Calculation type: Arithmetic Operations"
