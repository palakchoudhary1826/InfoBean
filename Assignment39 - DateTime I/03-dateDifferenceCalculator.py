'''
Docstring for 03-dateDifferenceCalculator


Assignment 3 — Date Difference Calculator

Create a program that accepts two dates and displays:

Enter first date: 10-09-2026
Enter second date: 25-12-2026

Display:

Difference in days
Difference in weeks
Difference in hours
Difference in minutes

Example:

Days Difference: 106
Weeks Difference: 15
Hours Difference: 2544
Minutes Difference: 152640
'''

from datetime import date,datetime

d1,m1,y1=map(int,input("Enter First date (DD-MM-YYYY) : ").split("-"))
d2,m2,y2=map(int,input("Enter Second date (DD-MM-YYYY) : ").split("-"))



date1=date(y1,m1,d1)
print(date1)
date2=date(y2,m2,d2)
print(date2)


diff=date2-date1
print(f"Days Difference : {diff.days}")


week=diff.days//7
print(f"Week difference : {week}")

hrs=diff.days*(24)
print(f"Hours Difference : {hrs}")

min=diff.days*(24)*(60)
print(f"Minutes Difference : {min}")
