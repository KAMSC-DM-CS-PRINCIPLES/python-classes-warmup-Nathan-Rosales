# TODO create class BankAccount

class BankAccount:
        def __init__(self,balance=0):
            self.balance = balance

        def deposit(self,dep):
            if dep > 0:
                self.balance += dep
            return self.balance
        
        def withdraw(self,draw):
            if self.balance-draw >= 0:
                self.balance -= draw
                return self.balance
            else:
                return "Insufficient Funds"
            
        def get_balance(self):
            return self.balance

if __name__ == "__main__":
    # create BankAccount below this
    bank123 = BankAccount(0)
    print(bank123.withdraw(100))