'''
Banking Fraud Detection System

A bank monitors transactions based on amount, location, OTP verification, and account age.

If transaction amount is at least 10000, then check location. If international, then check OTP verification. If verified, allow; otherwise block. If location is domestic, then check if amount is at least 50000. If yes, check account age. If account age is at least 2 years, allow; otherwise flag. If amount is less than 50000, allow. If transaction amount is less than 10000, then check unusual activity. If yes, flag; otherwise allow.

Input:
Transaction Amount = 60000
Location = domestic
Account Age = 1

Output:
Transaction Status = Flagged
'''
amt=int(input("Enter The Amount : "))
status=""

if amt>=10000:
    location=input("Enter The Location : (international/domestic) : ").lower()
    if location=="international":
        otp=input("Verify Your OTP (yes/no) : ").lower()
        if otp=="yes":
            status="allow"
        else:
            status="block"
    else:
        if amt>=50000:
            accountAge=int(input("Enter The Account Age : "))
            if accountAge>=2:
                status="allow"
            else:
                status="flagged"
        else:
            status="allow"
else:
    activity=input("is there any unsual activity (yes/no): ").lower()
    if activity=="yes":
        status="block"
    else:
        status="allow"

print(status)