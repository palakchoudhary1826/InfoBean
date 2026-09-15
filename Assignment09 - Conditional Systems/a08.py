'''
1. Smart Credit Card Approval System

A bank evaluates credit card applications based on income, credit score, employment type, and existing debt.

If income is greater than or equal to 50000, then check credit score. If credit score is greater than or equal to 750, then check debt. If debt is less than 20000, approve Premium Card; otherwise approve Gold Card. If credit score is less than 750, then check employment type. If employment is government and credit score is at least 650, approve Gold Card; otherwise reject.

If income is less than 50000, then check if income is at least 30000 and credit score is at least 700. If yes, approve Silver Card; otherwise reject.

Input:
Income = 45000
Credit Score = 720
Employment = private
Debt = 10000

Output:
Card Type = Silver Card
'''

income = int(input("Enter Income: "))
credit_score = int(input("Enter Credit Score: "))
# employment_type = input("Enter Employment Type (government/private): ").lower()
# debt = int(input("Enter Existing Debt: "))
approve=""

if income >= 50000:   
    if credit_score >=750 :
        debt = int(input("Enter Existing Debt: "))
        if debt<20000:
            approve="premium card"
        else:
            approve="gold card"
    else:
        employment_type = input("Enter Employment Type (government/private): ").lower()
        if employment_type=="government":
            
            if credit_score>=650:
                approve="gold card"
            else:
                approve="reject"
else:
    if income>=30000 and credit_score>=700:
        approve="silver card"
    else:
        approve="reject"


print(f"Card Type = {approve}")

