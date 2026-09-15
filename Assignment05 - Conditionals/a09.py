'''

Library Access System
   A library checks:

* If membership is active → Entry allowed
* If books issued < 3 → Can issue more books

Input:
Membership active (yes/no): yes
Books issued: 2

Output:
Entry allowed
Can issue more books
'''

memberShip=input("is your membership active ? (yes/no) : ").lower()
bookIssue=int(input("Enter The Number Of Book Issued : "))

if memberShip=="yes":
    print("Entry Allowed")
    if bookIssue<3:
        print("can issue more books")
    else:
        print("can not issue books")

else:
    print("Entry Not Allowed")