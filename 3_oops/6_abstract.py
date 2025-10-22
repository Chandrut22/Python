from abc import ABC, abstractmethod

# 1. Create the Abstract Base Class to define a contract
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        """
        A contract for all payment methods.
        They MUST implement this method.
        """
        pass

# 2. Create Concrete Implementations
class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing ₹{amount} through Credit Card. Applying transaction fee...")
        return "Credit Card payment successful."

class UpiPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing ₹{amount} through UPI. Initiating bank transfer...")
        return "UPI payment successful."

# --- A function that works with ANY payment method that follows the contract ---
def execute_payment(payment_method, amount):
    """
    This function doesn't need to know the details of how the payment is processed.
    It just needs to know that the object has a .process_payment() method.
    """
    print("--- New Transaction ---")
    result = payment_method.process_payment(amount)
    print(f"Result: {result}")

# --- Using the system ---
credit_card = CreditCardPayment()
upi = UpiPayment()

execute_payment(credit_card, 2500)
execute_payment(upi, 800)