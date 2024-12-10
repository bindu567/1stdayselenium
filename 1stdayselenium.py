class bankaccount:
    def __init__(self,account_holder,balance=0):
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"deposited{amount}.New balance:{self.balance}")
    def withdraw(self,amount):
        if amount>self.balance:
            print(f"insufficient funds!Current balance:{self.balance}")
        else:
            self.balance-=amount
            print(f"withdraw{amount}.New balance:{self.balance}")
account=bankaccount(account_holder="raghavendra",balance=19)
account.deposit(5)
account.withdraw(5)
