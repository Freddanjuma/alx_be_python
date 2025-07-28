class BankAccount:
    def __init__(self, balance=100):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${int(amount)}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${int(amount)}")

    def display_balance(self):
        print(f"Current Balance: ${int(self.balance)}")
