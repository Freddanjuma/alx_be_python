num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose an operation (add/subtract/multiply/divide): ").lower()

match operation:
    case "add":
        print(f"The result of addition is: {num1 + num2}")
    case "subtract":
        print(f"The result of subtraction is: {num1 - num2}")
    case "multiply":
        print(f"The result of multiplication is: {num1 * num2}")
    case "divide":
        if num2 != 0:
            print(f"The result of division is: {num1 / num2}")
        else:
            print("Cannot divide by zero!")
    case _:
        print("Invalid operation selected.")