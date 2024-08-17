class ATM:
    def __init__(self, initial_balance=0, pin="1234"):
        """Initialize the ATM with an initial balance and a default PIN."""
        self.balance = initial_balance
        self.pin = pin
        self.transaction_history = []

    def verify_pin(self):
        """Prompt the user to enter their PIN and verify it."""
        attempts = 3
        while attempts > 0:
            entered_pin = input("Enter your PIN: ")
            if entered_pin == self.pin:
                return True
            else:
                attempts -= 1
                print(f"Incorrect PIN. You have {attempts} attempt(s) left.")
        print("Too many incorrect attempts. Exiting...")
        return False

    def check_balance(self):
        """Display the current account balance."""
        print(f"Your current balance is: ${self.balance:.2f}")
        self.transaction_history.append(f"Balance inquiry: ${self.balance:.2f}")

    def deposit_cash(self):
        """Allow the user to deposit cash into their account."""
        try:
            amount = float(input("Enter the amount to deposit: $"))
            if amount > 0:
                self.balance += amount
                print(f"${amount:.2f} deposited successfully.")
                self.transaction_history.append(f"Deposited: ${amount:.2f}")
            else:
                print("Invalid amount. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def withdraw_cash(self):
        """Allow the user to withdraw cash from their account."""
        try:
            amount = float(input("Enter the amount to withdraw: $"))
            if 0 < amount <= self.balance:
                self.balance -= amount
                print(f"${amount:.2f} withdrawn successfully.")
                self.transaction_history.append(f"Withdrew: ${amount:.2f}")
            elif amount > self.balance:
                print("Insufficient balance.")
            else:
                print("Invalid amount. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def change_pin(self):
        """Allow the user to change their PIN."""
        old_pin = input("Enter your current PIN: ")
        if old_pin == self.pin:
            new_pin = input("Enter your new PIN: ")
            confirm_pin = input("Confirm your new PIN: ")
            if new_pin == confirm_pin:
                self.pin = new_pin
                print("PIN changed successfully.")
                self.transaction_history.append("PIN changed")
            else:
                print("PINs do not match. Try again.")
        else:
            print("Incorrect PIN. PIN change failed.")

    def show_transaction_history(self):
        """Display the transaction history."""
        if self.transaction_history:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions yet.")

    def run(self):
        """Run the ATM simulation."""
        if self.verify_pin():
            while True:
                print("\nATM Menu:")
                print("1. Check Balance")
                print("2. Deposit Cash")
                print("3. Withdraw Cash")
                print("4. Change PIN")
                print("5. View Transaction History")
                print("6. Exit")

                choice = input("Choose an option: ")

                if choice == "1":
                    self.check_balance()
                elif choice == "2":
                    self.deposit_cash()
                elif choice == "3":
                    self.withdraw_cash()
                elif choice == "4":
                    self.change_pin()
                elif choice == "5":
                    self.show_transaction_history()
                elif choice == "6":
                    print("Thank you for using the ATM. Goodbye!")
                    break
                else:
                    print("Invalid option. Please try again.")

# Run the ATM simulation
atm = ATM(initial_balance=1000)
atm.run()

