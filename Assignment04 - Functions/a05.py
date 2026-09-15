'''
Assignment 5: Salary Breakdown

An employee wants to calculate salary per day and per hour.

Input:
Monthly salary = 36000
Working days = 24
Working hours per day = 8

Expected Output:
Salary per day = 1500.0
Salary per hour = 187.5


'''

monthSalary=int(input("Enter The Salary :- "))
workDays=int(input("Enter The Work Day :- "))
workHrs=int(input("Enter The Work Hrs Per Day :- "))
a=monthSalary/workDays
print(f"Salary Per Day :- {a}")
print(f"Salary Per Day :- {a/workHrs}")