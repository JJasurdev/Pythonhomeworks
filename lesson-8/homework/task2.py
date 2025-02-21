import json

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance: {self.balance}"
        return "Invalid deposit amount."
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrawn {amount}. New balance: {self.balance}"
        return "Insufficient funds or invalid amount."
    
    def to_dict(self):
        return {"account_number": self.account_number, "name": self.name, "balance": self.balance}

class Bank:
    def __init__(self, filename="accounts.txt"):
        self.accounts = {}
        self.filename = filename
        self.load_from_file()
    
    def create_account(self, name, initial_deposit):
        account_number = str(len(self.accounts) + 1).zfill(6)
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        self.save_to_file()
        return f"Account created: {account_number}, Name: {name}, Balance: {initial_deposit}"
    
    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        return vars(account) if account else "Account not found."
    
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            result = self.accounts[account_number].deposit(amount)
            self.save_to_file()
            return result
        return "Account not found."
    
    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            result = self.accounts[account_number].withdraw(amount)
            self.save_to_file()
            return result
        return "Account not found."
    
    def save_to_file(self):
        with open(self.filename, "w") as f:
            json.dump({acc: self.accounts[acc].to_dict() for acc in self.accounts}, f)
    
    def load_from_file(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.accounts = {acc: Account(**data[acc]) for acc in data}
        except (FileNotFoundError, json.JSONDecodeError):
            self.accounts = {}


