from atm_package.transaction import add_transaction
from datetime import datetime


class ATMAccount:
    def __init__(self):
        self.balance = 10000
        self.transaction_history = []

    def show_balance(self):
        print(f"\nCurrent Balance: ₹{self.balance}")

    def deposit_money(self, amount):
        if amount <= 0:
            print("Deposit amount should be greater than 0.")
            return

        self.balance += amount

        transaction = (
            f"Deposited ₹{amount} on "
            f"{datetime.now().strftime('%d-%m-%Y %I:%M %p')}"
        )

        add_transaction(self.transaction_history, transaction)

        print(f"₹{amount} deposited successfully.")
        print(f"Updated Balance: ₹{self.balance}")

    def withdraw_money(self, amount):
        if amount <= 0:
            print("Enter a valid amount.")
            return

        if amount > self.balance:
            print("Insufficient balance!")
            return

        self.balance -= amount

        transaction = (
            f"Withdrawn ₹{amount} on "
            f"{datetime.now().strftime('%d-%m-%Y %I:%M %p')}"
        )

        add_transaction(self.transaction_history, transaction)

        print(f"₹{amount} withdrawn successfully.")
        print(f"Remaining Balance: ₹{self.balance}")

    def show_transactions(self):
        print("\n----- TRANSACTION HISTORY -----")

        if not self.transaction_history:
            print("No transactions found.")

        else:
            for item in self.transaction_history:
                print(item)

        print("--------------------------------")