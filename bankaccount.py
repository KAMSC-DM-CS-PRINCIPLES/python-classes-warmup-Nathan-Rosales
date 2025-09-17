# TODO create class BankAccount

if __name__ == "__main__":
    # create BankAccount below this

    class BankAccount:
        def __init__(self,balance):
            self.balance = balance

        def deposit(self,dep):
            if dep > 0:
                self.balance += dep
            return self.balance
        
        def withdraw(self,draw):
            if draw > 0:
                self.balance -= draw
                return self.balance
            else:
                return "Insufficient Funds"
            
        def get_balance(self):
            return self.balance