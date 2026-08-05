class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

def main():
    account = Account()
    print("Initial balance:", account.balance())
    
    account.deposit(100)
    print("Balance after deposit of 100:", account.balance())
    
    account.withdraw(50)
    print("Balance after withdrawal of 50:", account.balance())
    
if __name__ == "__main__":
    main()