'''ASSIGNMENT 2 — BANK ACCOUNT MANAGEMENT SYSTEM
=============================================
A bank provides different types of accounts.
Create the following hierarchy:
Account
|
+-------- SavingsAccount
|
+-------- PremiumSavingsAccount
REQUIREMENTS:
1. Create a parent class Account.
Attributes:
* account_number
* customer_name
* balance

2. SavingsAccount should inherit from Account.
Additional attribute:
* interest_rate

3. PremiumSavingsAccount should inherit from SavingsAccount.
Additional attribute:
* cashback_percentage

4. Parent-class data must be initialized using super().

5. Create the following methods:
display_account()
deposit()
withdraw()

6. Override display_account() in SavingsAccount.

7. Override display_account() again in PremiumSavingsAccount.

8. Each overridden method must call the parent method using super().

9. Demonstrate multilevel inheritance.

10. Balance must be encapsulated using:
@property
@balance.setter
@balance.deleter

11. Balance cannot be negative.

12. Read all data from the user.

INPUT:
Enter Account Number:
Enter Customer Name:
Enter Initial Balance:
Enter Account Type:

1. Savings Account
2. Premium Savings Account
For Savings Account:

Enter Interest Rate:

For Premium Savings Account:

Enter Interest Rate:
Enter Cashback Percentage:

Then ask:

Enter amount to deposit:
Enter amount to withdraw:

SAMPLE INPUT:

Enter Account Number: 1001
Enter Customer Name: Amit
Enter Initial Balance: 25000
Enter Account Type: 2
Enter Interest Rate: 7
Enter Cashback Percentage: 2
Enter amount to deposit: 5000
Enter amount to withdraw: 3000

EXPECTED OUTPUT:

## Account Details

Account Number: 1001
Customer Name: Amit
Balance: 25000

Account Type: Premium Savings Account
Interest Rate: 7%
Cashback Percentage: 2%

After Deposit:
Balance: 30000

After Withdrawal:
Balance: 27000
'''
class Account:
    def __init__(self,account_number,customer_name,balance):
        self.number=account_number
        self.name=customer_name
        self.__amount=balance

    @property
    def balance(self):
        return self.__amount

    @balance.setter
    def balance(self,amount):
        if amount>=0:
            self.__amount=amount
        else:
            print("Balance Must be Greater than 0")

    @balance.deleter
    def balance(self):
        del self.__amount
        

    def display_account(self):
        print(f"""Account Number: {self.number}
Customer Name: {self.name}
Balance: {self.__amount}""")

    def deposit(self,x):
        if x>0:
            self.__amount+=x
            print("\nAfter Deposit:")
            print(self.__amount)
        else:
            print("Invalid Amount")

    def withdraw(self,y):
        if y>0:
            if self.__amount<y:
                print("Withdrawal is not possible")
            else:
                self.__amount=self.__amount - y
                print("\nAfter Withdrawal:")
                print(self.__amount)
        else:
            print("Invalid Amount")


class SavingsAccount(Account):
    def __init__(self,account_number,customer_name,balance,interest_rate):
        super().__init__(account_number,customer_name,balance)
        self.bal=interest_rate

    def display_account(self):
        super().display_account()
        print("Account Type: Saving Account")
        print("Interest Rate: ",self.bal)



class PremiumSavingAccount(SavingsAccount):
    def __init__(self,account_number,customer_name,balance,interest_rate,cashback_percentage):
        super().__init__(account_number,customer_name,balance,interest_rate)
        self.c_percentage=cashback_percentage

    def display_account(self):
        super().display_account()
        print("Account Type: Premium Saving Account")
        print("Interest Rate: ",self.bal)
        print("Cashback Percentage: ",self.c_percentage)

number=int(input("Enter Account Number:"))
name=input("Enter Customer Name:")
balance=int(input("Enter Initial Balance:"))
print("""Account Type:
1. Saving Account
2. Premium Saving Account""")
type=int(input("Enter Account type:"))
match type:
    case 1:
        interest_rate=float(input("Enter Interest Rate:"))
        amount=int(input("Enter Amount to Deposit:"))
        amount1=int(input("Enter Amount to Withdraw:"))
        s=SavingsAccount(number,name,balance,interest_rate)
        s.display_account()
        s.deposit(amount)
        s.withdraw(amount1)
    case 2:
        interest_rate=float(input("Enter Interest Rate:"))
        cashback_percentage=int(input("Enter Cashback Percentage:"))
        amount=int(input("Enter Amount to Deposit:"))
        amount1=int(input("Enter Amount to Withdraw:"))
        p=PremiumSavingAccount(number,name,balance,interest_rate,cashback_percentage)
        p.display_account()
        p.deposit(amount)
        p.withdraw(amount1)
    case __:
        print("Invalid Choice")