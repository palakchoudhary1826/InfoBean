'''
Assignment 10: Percentage Calculator

Write a Python program that:

Accepts total marks and obtained marks.
Calculates percentage.

Input:
Total = 500
Obtained = 400

Output:
Percentage = 80%

'''

total=int(input("Enter The Total Marks : "))
obtained=int(input("Enter The Obtained Marks : "))

print(f"Percentage : {(obtained/total)*100}")