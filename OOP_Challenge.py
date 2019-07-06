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

account1 = Account('Siddharth', 100)
print(account1)
print(account1.owner)
print(account1.balance)