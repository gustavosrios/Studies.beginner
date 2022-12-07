class Account:
    def __init__(self,owner, balance):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'
    def deposit(self,value):
        print('Deposit Accepted')
        self.balance += value
        print(f'Current Balance: {self.balance}')
    def withdraw(self,value):
        if self.balance < value:
            print(f'Funds Unavailable!\nCurrent Balance: {self.balance}\nWithdraw requested: {value}')
        else:
            print('Withdraw Accepted')
            self.balance -= value
            print(f'Current Balance: {self.balance}')
acct1 = Account('Jose', 100)
#print(acct1)
acct1.deposit(50)
acct1.withdraw(500)
print(f'{acct1.owner}')
print(f'{acct1.balance}')