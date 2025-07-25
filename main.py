shopping_list = ["Milk", "Bread", "Eggs", "Butter"]

def display_menu():
    print("Shopping List Menu")
    print("1. View items")
    print("2. Add item")
    print("3. Remove item")
    print("4. Exit")

display_menu()

choice = int(input("Enter your choice (1-4): "))
print(f"You selected option {choice}")from arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
