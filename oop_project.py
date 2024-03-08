from bank_accounts import *
James=Bank_account(200000,"James")
Harrison=Bank_account(40000,"Harrison")
Sara=Bank_account(4000,"Sara")

James.getbalance()
Harrison.getbalance()
Sara.getbalance()

James.deposit(50000)
Harrison.deposit(900000)
Sara.deposit(500000)

James.withdraw(10)
Harrison.withdraw(30)

James.transfer(200,Harrison)

Sara.deposit(2000)
James.deposit(200000000)
Harrison.deposit(2000987088)

Jim=InterestRewardsAccount(1000,"Jim")
Jim.getbalance()
Jim.deposit(100)
Jim.transfer(100,James)


Blaze=savingsAccount(10000,"blaze")
Blaze.getbalance()
Blaze.withdraw(100)