import sys
from bank_account import BankAccount

account = BankAccount()  # Default $100

if len(sys.argv) < 2:
    print("Usage: python main-0.py <operation>:<amount> OR display")
    sys.exit(1)

arg = sys.argv[1].lower()

if arg == "display":
    account.display_balance()

elif ":" in arg:
    operation, amount_str = arg.split(":")
    try:
        amount = int(amount_str)
    except ValueError:
        print("Invalid amount.")
        sys.exit(1)

    if operation == "deposit":
        account.deposit(amount)
    elif operation == "withdraw":
        account.withdraw(amount)
    else:
        print("Unknown operation.")
else:
    print("Invalid command format. Use deposit:<amount>, withdraw:<amount>, or display.")
