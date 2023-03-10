class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self


    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
                self.balance -= amount
        else:
            print("Insufficient Funds: Charging $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    
    def yeild_interest(self):
        if self.balance > 0:
            self.balance +=(self.balance * self.int_rate)
        return self


savings = BankAccount(.03, 700)
checking = BankAccount(.06, 4000)


savings.deposit(20).deposit(10).deposit(30).withdraw(60).yeild_interest().display_account_info()
checking.deposit(70).deposit(90).deposit(300).withdraw(15).yeild_interest().display_account_info()