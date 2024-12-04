class BankAccount:
    def __init__(self, balance=0):
        self.balance = int(balance)

    def deposit(self, amount):
        if amount > 0: 
            self.balance += amount
        return int(self.balance)

    def withdraw(self, amount):
        if 0 < amount <= self.balance:  
            self.balance -= amount
        return int(self.balance)    