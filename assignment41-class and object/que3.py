"""Assignment 3: Bank Account Operations
 A bank wants to perform basic operations on a customer's account.

Create a class BankAccount with the following attributes:

Account number

Account holder name

Balance

Create the following methods:

deposit() – Add an amount to the balance.

withdraw() – Subtract an amount from the balance.

display_account() – Display account details and final balance.

Sample data:

Account Number: 1001
Account Holder: Rahul
Opening Balance: 25000
Deposit: 5000
Withdrawal: 3000

Expected result:

Final Balance: 27000

"""

class bankaccount:
    def accept(self,account_no,holder_name,balance):
        self.account_no=account_no
        self.holder_name=holder_name
        self.balance=balance
        
    def deposit(self,deposit_b):
        self.deposit_b=deposit_b
        self.balance=self.balance+self.deposit_b
    def withdraw(self,withdrawn_b):
        self.withdrawn_b=withdrawn_b
        self.balance=self.balance-self.withdrawn_b
    def display(self):
        print("Account Number=",self.account_no)
        print("Account Holder=",self.holder_name)
        print("Opening Balance= 25000")
        print("Deposit=",self.deposit_b)
        print("withdrawal",self.withdrawn_b)
        print("Final balance=",self.balance)
b=bankaccount()
b.accept(1001,"rahul",25000)
b.deposit(5000)
b.withdraw(3000)
b.display()

        