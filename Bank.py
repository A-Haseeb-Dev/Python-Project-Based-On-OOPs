from abc import ABC, abstractmethod

# ====================================
# ABSTRACTION: Base Account Class
# ====================================
class Account(ABC):
    def __init__(self, name, pin, balance=0):
        self.name = name
        self.__pin = pin            # Private → Encapsulation
        self.__balance = balance    # Private → Encapsulation

    # Getter (Encapsulation - Controlled Access)
    def get_balance(self):
        return self.__balance

    # Deposit Money
    def deposit(self, amount):
        self.__balance += amount
        return f"Deposited Rs.{amount}. New Balance: Rs.{self.__balance}"

    # Withdraw Money
    def withdraw(self, amount, pin):
        if pin != self.__pin:
            return "Incorrect PIN! Withdrawal failed."
        if amount > self.__balance:
            return "Insufficient balance!"
        self.__balance -= amount
        return f"Withdrawn Rs.{amount}. New Balance: Rs.{self.__balance}"

    # Transfer Money
    def transfer(self, other_account, amount, pin):
        if pin != self.__pin:
            return "Incorrect PIN! Transfer failed."
        if amount > self.__balance:
            return "Insufficient balance for transfer."
        self.__balance -= amount
        other_account.__balance += amount     # Direct access (allowed inside class)
        return f"🔁 Transferred Rs.{amount} to {other_account.name}"

    @abstractmethod
    def calculateInterest(self):  # Polymorphism
        pass


# ====================================
# INHERITANCE + POLYMORPHISM
# ====================================
class SavingsAccount(Account):
    def calculateInterest(self):
        interest = self.get_balance() * 0.05  # 5% interest
        return f"Savings Account Interest: Rs.{interest}"


class CurrentAccount(Account):
    def calculateInterest(self):
        return "Current Account has NO interest!"


# ====================================
# BANK SYSTEM (Manage Accounts)
# ====================================
class BankSystem:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def show_accounts(self):
        print("\nBank Accounts:")
        for acc in self.accounts:
            print(f"- {acc.name} → Balance: Rs.{acc.get_balance()}")
        print()


# ====================================
# DEMO / TESTING
# ====================================
bank = BankSystem()

# Create Accounts
acc1 = SavingsAccount("Ali", 1234, 5000)
acc2 = CurrentAccount("Sara", 4321, 9000)

bank.add_account(acc1)
bank.add_account(acc2)

bank.show_accounts()

# Deposit & Withdraw
print(acc1.deposit(1000))
print(acc1.withdraw(3000, 1234))
print(acc2.withdraw(2000, 4321))

# Transfer Money
print(acc1.transfer(acc2, 1000, 1234))

# Interest (Polymorphism in action!)
print(acc1.calculateInterest())
print(acc2.calculateInterest())

bank.show_accounts()
