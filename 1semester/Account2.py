class Account:
    """docstring"""
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount
        self.transactions = 0

    def deposit(self, amount):
        self.balance += amount
        self.transactions += 1

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions += 1

    def dump(self):
        s = 'account holder: %s,\naccount no. %s,\nbalance: %s,\ntransactions: %s' % \
            (self.name, self.no, self.balance, self.transactions)
        print s
