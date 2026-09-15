'''
Docstring for Assignment09.a13
Banking Fraud Detection System

A bank checks fraud risk based on transaction amount, location, device, and transaction count.

If amount is greater than or equal to 50000, then check location. If location is international, then check device. If device is new, then check transaction count. If transactions are more than 3, mark High Risk (Block); otherwise Medium Risk. If device is not new, mark Medium Risk.

If location is domestic, then check transaction count. If more than 5, mark Medium Risk; otherwise Low Risk.

If amount is less than 50000, then check unusual activity. If yes, then check device. If device is new, mark Medium Risk; otherwise Low Risk. If no unusual activity, mark Safe.

Input:
Amount = 70000
Location = international
Device = new
Transactions = 4

Output:
Risk Level = High Risk (Blocked)
'''
amount = int(input("Enter Transaction Amount: "))
# location = input("Enter Location (international/domestic): ").lower()
device = input("Enter Device (new/old): ").lower()
# transactions = int(input("Enter Transaction Count: "))

mark=""


if amount >= 50000:
    location = input("Enter Location (international/domestic): ").lower()
    transactions = int(input("Enter Transaction Count: "))
    if location=="international":
       
        if device=="new":
            if transactions>3:
                mark="high risk  (Block)"
            else:
                mark="medium risk "
        else:
            mark="medium risk"
    else:
        if transactions>5:
            mark="medium risk"
        else:
            mark="low risk"
else:
    unusual_activity = input("Is there Unusual Activity? (yes/no): ").lower()
    if unusual_activity=="yes":
        if device=="new":
            mark="medium risk"
        else:
            mark="low risk"
    else:
        mark="safe"
print(f"Risk Level : High Risk (Blocked)")


