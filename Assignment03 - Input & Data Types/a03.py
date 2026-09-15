'''

Assignment 3: Electricity Bill Calculator

Write a Python program that:

Accepts number of units.
Calculates bill (₹6 per unit).

Input:
Units = 100

Output:
Bill = 600
'''

unit=int(input("Enter The Unit Of Your Bill :- "))
print(f"Units : {unit} ")
print(f"Bill : {unit * 6}")