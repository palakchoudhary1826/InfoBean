'''
Docstring for Assignment09.a10
Smart Scholarship Allocation System

A scholarship is provided based on marks, family income, and category.

If marks are 85 or above, then check income. If income is less than or equal to 300000, then check category. If category is not general, give Full Scholarship; otherwise give 75% Scholarship. If income is above 300000, give 50% Scholarship.

If marks are between 70 and 84, then check income. If income is less than or equal to 200000, give 50% Scholarship; otherwise give 25% Scholarship.

If marks are below 70, no scholarship is given.

Input:
Marks = 88
Income = 250000
Category = OBC

Output:
Scholarship = Full Scholarship
'''
marks = int(input("Enter Marks: "))
income = int(input("Enter Family Income: "))
category = input("Enter Category (General/OBC/SC/ST): ").lower()

if marks>=85:
    if income<=300000:
        if category!="general":
            s="full scholarship"
        else:
            s="75% scholarship"
    else:
        s="50% scholarship"
else:
    if marks>=70 and marks<=84:
        if income <=200000:
            s="50% scholarship"
        else:
            s="25% scholarship"
    else:
        s="no scholarship"

print(f"Scholarship : {s}")