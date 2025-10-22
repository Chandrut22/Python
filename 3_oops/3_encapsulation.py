class Wallet:
    def __init__(self, owner, initial_amount=0):
        # '__' makes this attribute private
        self.__balance = initial_amount
        # '_' makes this attribute protected
        self._owner = owner
        print(f"Wallet for {self._owner} created with initial balance of ₹{self.__balance}")

    # Public method to add money
    def add_money(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Added ₹{amount}. New balance is ₹{self.__balance}.")
        else:
            print("Amount to add must be positive.")

    # Public method to spend money
    def spend_money(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Spent ₹{amount}. Remaining balance is ₹{self.__balance}.")
        elif amount > self.__balance:
            print("Transaction failed. Insufficient funds.")
        else:
            print("Amount to spend must be positive.")
    
    # Public method to check the balance
    def check_balance(self):
        return f"The current balance is ₹{self.__balance}."
        
    # Public method to get the owner's name
    def get_owner(self):
        return f"This wallet belongs to {self._owner}."


# --- Using the encapsulated class ---
my_wallet = Wallet("Rohan", 500)

print("\n--- Transactions ---")
my_wallet.add_money(200)
my_wallet.spend_money(100)
my_wallet.spend_money(700) # This will fail due to the internal check

# --- Accessing the protected variable ---
# While possible, direct access is discouraged by convention.
print(f"\nDirectly accessing protected var (discouraged): {my_wallet._owner}")

# The correct way is to use a public method if provided.
print(f"Accessing via public method: {my_wallet.get_owner()}")


# --- Accessing the private variable ---
# Trying to access the private balance directly still causes an AttributeError
try:
    print(f"\nTrying to access private balance: {my_wallet.__balance}")
except AttributeError as e:
    print(f"Error: {e}")

# We can only check the balance through the public method
print(my_wallet.check_balance())