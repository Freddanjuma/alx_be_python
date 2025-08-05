class Calculator:
    calculation_type = "Arithmetic Operations"  # Class variable

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def display_calculation_type(cls):
        print(f"Calculation type: {cls.calculation_type}")
