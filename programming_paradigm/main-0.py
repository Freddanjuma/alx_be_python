import sys
from bank_account import BankAccount

if len(sys.argv) < 2:
    print("Usage: python3 main.py <operation> [amount]")
    sys.exit(1)

operation = sys.argv[1]
account = BankAccount(500)

if operation == "deposit":
    if len(sys.argv) != 3:
        print("Usage: python3 main.py deposit <amount>")
        sys.exit(1)
    amount = float(sys.argv[2])
    account.deposit(amount)
    account.display_balance()

elif operation == "withdraw":
    if len(sys.argv) != 3:
        print("Usage: python3 main.py withdraw <amount>")
        sys.exit(1)
    amount = float(sys.argv[2])
    if account.withdraw(amount):
        print("Withdrawal successful.")
    else:
        print("Insufficient funds.")
    account.display_balance()

elif operation == "balance":
    account.display_balance()

else:
    print("Unknown operation. Use 'deposit', 'withdraw', or 'balance'.")
