class BankAccount:
    """Represents a basic bank account with common
    operations like deposit, withdraw, balance display."""
    def __init__(self, account_number, account_holder, initial_balance=0):
        """Initilize the new bank account instance"""
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = initial_balance

    def deposite(self, amount):
        """Deposits funds into the account.the positive amount deposite"""
        if amount > 0:
            self._balance += amount
            print(f"Deposite amount is = {amount}")
        else:
            print("Deposite amount must be positive")

    def withdraw(self, amount):
        """Withdraws funds from the account if sufficient
        balance exists.The positive amount withdraw.
        return True if withdrawal is successfull otherwise False"""
        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
                print(f"Withdraw amount is= {amount}")
                return True
            else:
                print("Insufficient fund")
                return False
        else:
            print("Withdraw amount must be positive")
            return False

    def display_balance(self):
        """print the current account details balance"""
        print(f"\n---Account Details---")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self._balance}")

class SavingsAccount(BankAccount):
    """
    Derived class for savings accounts with an interest rate.
    """
    def __init__(self, account_number, account_holder,
                 initial_balance=0, interest_rate=0.05):
        """Initialize the saving account instance"""
        super().__init__(account_number, account_holder, initial_balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        """Calculates interest based on the current balance.
        returns the float calculated interest amount"""
        interest = self._balance * self.interest_rate
        print(f"Calculated interest: {interest}.")
        return interest

    def apply_interest(self):
        """Applies the calculated interest to the account balance."""
        interest = self.calculate_interest()
        self.deposite(interest)
        print("Interest applied.",interest)

class CurrentAccount(BankAccount):
    """Represents a current account, inheriting from BankAccount,
     with overdraft capability."""
    def __init__(self, account_number, account_holder,
                 initial_balance=0, overdraft_limit=1000):
        """Initialize the current account instance"""
        super().__init__(account_number, account_holder, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """
        Modifies withdrawal to allow overdrafts within the specified limit.
        """
        if amount > 0:
            if amount <= self._balance + self.overdraft_limit:
                self._balance -= amount
                print(f"withdraw : {amount} new balance : {self._balance}")
                return True
            else:
                print(f"withdraw denied. overdraft limit : "
                      f"{self.overdraft_limit}")
                return False
        else:
            print("withdraw amount must be positive")
            return False

print("-------User input for saving account-----------")
# Get user input for account details
account_number = input("Enter Saving account number=")
account_holder = input("Enter account holder name=")
initial_balance = float(input("Enter initial balance for savings="))
interest_rate = float(input("Enter interest rate="))

print("\n------------Saving account Operations----------------")
savings = SavingsAccount(account_number, account_holder,
                         initial_balance, interest_rate)

amount = float(input("Enter amount to deposite="))
savings.deposite(amount)

amount = float(input("Enter amount to withdraw="))
savings.withdraw(amount)

savings.apply_interest()
savings.display_balance()

print("-------User input for current account-----------")
# Get user input for account details
account_number = input("Enter current account number=")
account_holder = input("Enter account holder name=")
initial_balance = float(input("Enter initial balance ="))
overdraft_limit = float(input("Enter overdraft limit="))

print("\n-----------Current account example-------------")
current = CurrentAccount(account_number, account_holder,
                         initial_balance, overdraft_limit)

amount = float(input("Enter amount to deposite="))
current.deposite(amount)

amount = float(input("Enter amount to withdraw="))
current.withdraw(amount)

current.display_balance()
