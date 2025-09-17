# TODO create class BankAccount

if __name__ == "__main__":
    # create BankAccount below this

    class BankAccount:
        def _init_(intial):
            if initial == null:
                raise ValueError
            else:
                balance = initial

    def deposit(dep):
        if dep > 0:
            balance += dep
        return balance
    
    def withdraw(draw):
        if draw > 0:
            balance -= draw
            return balance
        else:
            return "Insufficient Funds"
        
    def get_balance():
        return balance

    pass