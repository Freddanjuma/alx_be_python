shopping_list = ["Milk", "Bread", "Eggs", "Butter"]

def display_menu():
    print("\nShopping List Menu")
    print("1. View items")
    print("2. Add item")
    print("3. Remove item")
    print("4. Exit")

def view_items():
    print("\nYour Shopping List:")
    for index, item in enumerate(shopping_list, start=1):
        print(f"{index}. {item}")

def add_item():
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"{item} has been added to your shopping list.")

def remove_item():
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from your shopping list.")
    else:
        print(f"{item} is not in the shopping list.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            view_items()
        elif choice == '2':
            add_item()
        elif choice == '3':
            remove_item()
        elif choice == '4':
            print("Exiting Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()

