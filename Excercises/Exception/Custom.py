class Custom:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Cannot withdraw more than the available balance.")

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        self.balance -= amount
        print(f"Withdrawal successful. Remaining balance: {self.balance}")



class InsufficientFundsError(Exception):
    """Raised when an account has insufficient funds for a withdrawal."""
    pass

if __name__ == "__main__":
    customer = Custom(balance=1000)
    try:
        customer.withdraw(1500)
    except InsufficientFundsError as e: print(f"Error: {e}")

    try:
        customer.withdraw(-500)
    except ValueError as e:
        print(f"Error: {e}")
        customer.withdraw(500)