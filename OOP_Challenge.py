# Create a bank account class that has two attributes:

#   * owner
#   * balance

# and two methods

#   * deposit
#   * withdraw

# As an added requirement, withdrawals may not exceed the available balance.

class Account:

    def __init__(self, owner = 'Owner', balance = 0):

        self.owner = owner
        self.balance = balance

    def __str__(self):

        return f"Account owner : {self.owner} \nAccount balance : ${self.balance}"

    def deposit(self, deposit_amnt):

        self.balance = self.balance + deposit_amnt
        print('Deposit Accepted')

    def withdraw(self, withdraw_amnt):

        if self.balance < withdraw_amnt:
            print('Sorry! Funds Unavailable')
        else:
            self.balance = self.balance - withdraw_amnt
            print('Withdrawal Accepted')


account1 = Account('Siddharth', 100)
print(account1)

while True:

    ch = input('Do you wish to make a deposit? (y/n) ').lower()
    if ch == 'n':
        break
    else:
        deposit_ammount = int(input('Enter Ammount : '))
        account1.deposit(deposit_ammount)

print(account1)

while True:

    ch = input('Do you wish to withdraw amount? (y/n) ').lower()
    if ch == 'n':
        break
    else:
        withdrawal = int(input('Enter Amount : '))
        account1.withdraw(withdrawal)

print(account1)
