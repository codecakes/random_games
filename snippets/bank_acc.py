class BankAccount:
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.bal = initial_balance
        self.fee = 0

    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.bal += amount

    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        self.bal -= amount
        if self.bal < 0:
            self.fee += 5
            self.bal -= self.fee

    def get_balance(self):
        """Returns the current balance in the account."""
        return self.bal

    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.fee
