import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # You can change this for different test cases

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command_input = sys.argv[1]

    if command_input == "display":
        account.display_balance()
        return

    if ":" not in command_input:
        print("Invalid command format. Use <command>:<amount>")
        sys.exit(1)

    command, value = command_input.split(":", 1)

    try:
        amount = float(value)
    except ValueError:
        print("Amount must be a valid number.")
        sys.exit(1)

    if command == "deposit":
        account.deposit(amount)
        print(f"Deposited ${amount:.2f}")
    elif command == "withdraw":
        if account.withdraw(amount):
            print(f"Withdrew ${amount:.2f}")
        else:
            print("Insufficient funds.")
    else:
        print("Unknown command. Use deposit, withdraw, or display.")
        sys.exit(1)

    account.display_balance()

if __name__ == "__main__":
    main()
