class BankAccount:
    def __init__(self, balance):
        self._balance=balance #Private attribute

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print('Insufficient Funds')
    
    def get_balance(self):
        return self._balance
    
#create an object with initial balance
#Inherit
account = BankAccount(1000)

#print the current balance
print('current balance: ', account.get_balance())

#deposit 500 into the account
account.deposit(500)
print('Balance after deposit: ', account.get_balance())

#withdraw 200 from account
account.withdraw(200)
print('Balance after withdraw: ', account.get_balance())

#try withdraw more than the balance
account.withdraw(1500)