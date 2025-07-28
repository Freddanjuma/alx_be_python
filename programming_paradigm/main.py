import sys
from bank_account import BankAccount

account = BankAccount(500) 

if len(sys.argv) < 2:
    print("Usage: python3 main-0.py <operation> [amount]")
    sys.exit(1)

operation = sys.argv[1]

if operation == "deposit":
    if len(sys.argv) != 3:
        print("Please provide the amount to deposit.")
    else:
        amount = float(sys.argv[2])
        account.deposit(amount)
        account.display_balance()

elif operation == "withdraw":
    if len(sys.argv) != 3:
        print("Please provide the amount to withdraw.")
    else:
        amount = float(sys.argv[2])
        if account.withdraw(amount):
            print("Withdrawal successful.")
        else:
            print("Insufficient funds.")
        account.display_balance()

elif operation in ["balance", "display"]:  # Accept both
    account.display_balance()

else:
    print("Unknown operation. Use 'deposit', 'withdraw', or 'balance'.")
