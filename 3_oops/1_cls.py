class BankAccount:
    """A class to represent a simple bank account."""

    # Constructor to initialize the account
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        print(f"Account for {self.account_holder} created with initial balance of ₹{self.balance}.")

    # Method to add money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    # Method to remove money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")
        elif amount > self.balance:
            print(f"Withdrawal failed. Insufficient funds. You only have ₹{self.balance}.")
        else:
            print("Withdrawal amount must be positive.")

    # Method to display balance
    def check_balance(self):
        print(f"The current balance for {self.account_holder} is ₹{self.balance}.")


# --- Create and use a BankAccount object ---
my_account = BankAccount("Rohan Sharma", 5000)

print("\n--- Bank Transactions ---")
my_account.check_balance()
my_account.deposit(2500)
my_account.withdraw(1500)
my_account.withdraw(7000) # This will fail
my_account.check_balance()