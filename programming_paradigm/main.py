import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  

    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    user_input = sys.argv[1]

    if user_input == "display":
        account.display_balance()
        return

    if ":" not in user_input:
        print("Invalid input format. Expected <command>:<amount>")
        sys.exit(1)

    command, amount_str = user_input.split(":", 1)

    try:
        amount = float(amount_str)
    except ValueError:
        print("Amount must be a number.")
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
        print("Invalid command. Use deposit, withdraw, or display.")
        sys.exit(1)

    account.display_balance()

if __name__ == "__main__":
    main()
