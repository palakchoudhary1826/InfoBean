'''

10. Mobile Data Plan Advisor


A telecom company suggests the most suitable data plan based on a user’s daily data usage:

* More than 3GB/day → Premium Plan
* 1GB to 3GB/day → Standard Plan
* Less than 1GB/day → Basic Plan

Write a Python program to recommend a plan.

Input:
Enter daily data usage: 0.8

Output:
Recommended Plan: Basic Plan
'''

d=float(input("Enter The Daily Data Usage : "))

if d<1:
    print("Basic Plan")
elif d<=3:
    print("Standard Plan")
else:
    print("Premium Plan")