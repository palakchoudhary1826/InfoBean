'''
Docstring for a08
Question 8: ATM Note Counter

Write a program to:

Read the withdrawal amount.
Count the number of ₹100 notes required using a loop.

Input

700

Output

Notes = 7
'''
n=int(input("Enter The Amount : "))
note=0

while n>=100:
    note+=1
    n-=100

print(f"Notes :{note}")
