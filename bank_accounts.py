class BalanceException(Exception):
    pass

class Bank_account:
    def __init__(self, amount,acc_name):
        self.amount=amount
        self.acc_name=acc_name
        print(f"Account '{self.acc_name}' created:\nBalance = Ksh.{self.amount:.2f} ")
    def getbalance(self):
        print(f"\nAccount '{self.acc_name}', Balance=Ksh.{self.amount:.2f}")
    def deposit(self, deposit_amnt):
        self.amount=self.amount + deposit_amnt
        self.getbalance()
    def viable_transaction(self, amount):
        if self.amount >= amount:
            return
        else:
            raise BalanceException(f"Sorry, account'{self.name}' only has a balance of Ksh.{self.amount:.2f} ")
    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.amount=self.amount - amount
            print("\nWithdraw complete !")
            self.getbalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted : {error}')
    def transfer(self,amount,acc_name):
        try:
            print("\n**********\n\nTransfer initializing...🚀")
            self.viable_transaction(amount)
            self.withdraw(amount)
            acc_name.deposit(amount)
            print("\nTransfer complete ✅\n\n**********")
        except BalanceException as error:
            print(f'Transfer interrupted❌:{error}')
class InterestRewardsAccount(Bank_account):
    def deposit(self, deposit_amnt):
        self.amount=self.amount + (deposit_amnt*1.05)
        print('\nDeposit Complete')
        self.getbalance()
class savingsAccount(InterestRewardsAccount):
    def __init__(self,amount,acc_name):
        super().__init__(amount,acc_name)
        self.fee=5
    def withdraw(self,amount):
        try:
            self.viable_transaction(amount+self.fee)
            self.amount=self.amount-(amount+self.fee)
            print("\nWithdraw complete")
            self.getbalance()
        except BalanceException as error:
            print(f"Withdraw interrupted:{error}")
            