'''
Assignment 11: Time Duration Adder

Write a Python program that:

Accepts hours, minutes, seconds.
Converts into total seconds.

Input:
Hours = 1
Minutes = 2
Seconds = 30

Output:
Total Seconds = 3750

'''

hrs=int(input("Enter The Hours : "))
min=int(input("Enter The Minutes : "))
second=int(input("Enter The Seconds : "))
totalSeconds=(hrs*3600)+(min*60)+(second)
print(f"Total Seconds : {totalSeconds}")