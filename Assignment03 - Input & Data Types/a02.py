'''
Assignment 2: Salary Calculator

Write a Python program that:

Accepts daily wage and number of days.
Calculates total salary.

Input:
Daily wage = 500
Days = 26

Output:
Salary = 13000

'''
dailyWages=int(input("Enter The Daily Wage :- "))
days=int(input("Enter The Days :- "))

print(f"salary ={dailyWages * days}")
