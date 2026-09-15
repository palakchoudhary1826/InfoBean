'''
Assignment 2: Mobile EMI Calculation

You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.

Input:
Mobile price = 30000
Down payment = 5000
Interest rate = 10%
Months = 10

Expected Output:
Remaining Amount = 25000
Total with Interest = 27500
Monthly EMI = 2750.0
'''
mobilePrice=int(input("Enter The Mobile Price :- "))
downPayment=int(input("Enter The Down Payment :- "))
interestRate=int(input("Enter The Interest Rate :- "))
month=int(input("Enter The Month :- "))

remainAmt=mobilePrice-downPayment
interest=(remainAmt/100)*interestRate
totalWithInterest = remainAmt+interest
monthlyEmi=totalWithInterest/month

print(f"Remaining Amount :- {remainAmt}")
print(f"Total With Interest :- {totalWithInterest}")
print(f"Monthly EMI :- {monthlyEmi}")



