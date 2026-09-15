'''
========================================
Assignment 8: Simple Interest Calculator
========================================

A bank wants to help customers calculate the simple interest on their savings.

Write a Python program that:
- Accepts principal amount, rate of interest, and time (in years) as input.
- Calculates the simple interest using the formula:
  SI = (P × R × T) / 100
- Displays the simple interest.

Example:
Principal = 1000
Rate = 5
Time = 2
Simple Interest = 100.0
'''

p=int(input("Enter The Principal Amount : "))
r=int(input("Enter The Rate Of Interest : "))
t=int(input("Enter The Time(in yrs) : "))

si=float((p*r*t)/100)
print(" ")
print(f"Principal : {p}")
print(f"Rate Of Interest : {r}")
print(f"Time : {t} yrs")
print(f"Simple Interest :{si}")