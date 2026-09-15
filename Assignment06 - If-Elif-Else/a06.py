'''
6. Company Bonus Distribution System


A company wants to calculate bonuses for employees based on their years of experience:

* More than 10 years → 20% bonus
* 5 to 10 years → 10% bonus
* 2 to 5 years → 5% bonus
* Less than 2 years → No bonus

Write a Python program to calculate the bonus amount.

Input:
Enter salary: 50000
Enter years of experience: 6

Output:
Bonus Amount: ₹5000

'''

s=int(input("Enter The salary : "))
e=int(input("Enter The experience : "))
bonus=0

if e>=10:
    bonus=(s*20)/100
elif e<=10:
    bonus=(s*10)/100
elif e<=5:
    bonus=(s*5)/100
else:
    print("no bonus")

print(f"bonus amount : {bonus}")
    