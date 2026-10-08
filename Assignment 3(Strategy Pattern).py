from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str):
        self.card_number = card_number

    def pay(self, amount: float):
        print(f"Paid ${amount:.2f} using Credit Card ({self.card_number[-4:]}).")

class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float):
        print(f"Paid ${amount:.2f} using PayPal ({self.email}).")

# Context
class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def process_payment(self, amount: float):
        self._strategy.pay(amount)

# Driver Code
if __name__ == "__main__":
    processor = PaymentProcessor(CreditCardPayment("1234-5678-9012-3456"))
    processor.process_payment(100.50)

    # Dynamically change payment method
    processor.set_strategy(PayPalPayment("user@example.com"))
    processor.process_payment(49.99)
