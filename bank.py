class BankAccount:
    def __init__(self, init_bal):
        """Creates an account with the given balance."""
        self.init_bal = init_bal
        self.account = init_bal


    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.amount = amount
        self.account += amount


    def withdraw(self, amount):
       self.account -= amount

    def balance(self):
       print (self.account)
class SavingsAccount(BankAccount) : 
    def ZakatDeduction(self,amount):
       self.account=amount*0.25
       print(self.account)
class NonTaxFilerAccount(BankAccount):
    def withdraw(self, amount):
       self.account -= amount*(0.2)
       print(self.account)
x = BankAccount(700)
x.balance()
y=BankAccount
y.SavingsAccount(700)
z=BankAccount
z.withdraw(70)