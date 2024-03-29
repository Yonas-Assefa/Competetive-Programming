class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        no_account = len(self.balance)

        if (no_account > (account1 - 1)) and (no_account > (account2 - 1)):

            account1_balance = self.balance[account1 - 1]
            account2_balance = self.balance[account2 - 1]

            if (account1_balance >= money):

                self.balance[account1 - 1] -= money
                self.balance[account2 - 1] += money
                return True

            else:
                return False
        else:
            return False
       
    def deposit(self, account: int, money: int) -> bool:
        no_account = len(self.balance)

        if no_account >= account:
            self.balance[account - 1] += money
            return True

        else:
            return False

    def withdraw(self, account: int, money: int) -> bool:
        no_account = len(self.balance)

        if no_account >= account:

            if self.balance[account - 1] >= money:
                self.balance[account - 1] -= money
                return True

            else:
                return False
        else:
            return False
    
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)