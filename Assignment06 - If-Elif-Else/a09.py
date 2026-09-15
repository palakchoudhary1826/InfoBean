'''
9. Student Attendance Eligibility System

A college determines whether a student is eligible to sit for exams based on attendance percentage:

* 75% and above → Eligible
* 60% to 74% → Eligible with warning
* Below 60% → Not eligible

Write a Python program to check eligibility.

Input:
Enter attendance percentage: 58

Output:
Status: Not Eligible


'''

p=int(input("Enter The Attendance Percentage : "))

if p<60:
    print("Not Eligible")
elif p<=74:
    print("Eligible With Warning")
else:
    print(" eligible")