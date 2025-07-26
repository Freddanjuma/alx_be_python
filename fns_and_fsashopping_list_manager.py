shopping_list = []

def display_menu():
    print("\nShopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. Display list")
    print("4. Exit")

def add_item(item):
    shopping_list.append(item)
    print(f"'{item}' has been added to your shopping list.")

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from your shopping list.")
    else:
        print(f"'{item}' is not in the shopping list.")

def display_list():
    if shopping_list:
        print("\nYour shopping list:")
        for index, item in enumerate(shopping_list, 1):
            print(f"{index}. {item}")
    else:
        print("Your shopping list is empty.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            item = input("Enter item to add: ").strip()
            add_item(item)

        elif choice == '2':
            item = input("Enter item to remove: ").strip()
            remove_item(item)

        elif choice == '3':
            display_list()

        elif choice == '4':
            print("Exiting Shopping List Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please select between 1 and 4.")

if __name__ == "__main__":
    main()

