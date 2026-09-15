'''
Assignment 13: Compound Interest Calculator

Write a Python program that:

Accepts principal, rate, and time.
Calculates compound interest.

Input:
Principal = 1000
Rate = 10
Time = 2

Output:
Amount = 1210.0
Compound Interest = 210.0
'''

p=int(input("Enter the Principal: "))
r=int(input("Enter The Rate : "))
t=int(input("Enter The Time: "))

amount=p*((1+r/100)**t)
print(f"Amount : {int(amount)}")
print(f"Compound Gain : {int(amount)-p}")