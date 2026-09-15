'''
Assignment 5: Average Marks Calculator

Write a Python program that:

Accepts marks of 3 subjects.
Calculates average.

Input:
Marks = 80, 90, 70

Output:
Average = 80.0
'''


s1=int(input("Enter The Subject-1 : "))
s2=int(input("Enter The Subject-2 : "))
s3=int(input("Enter The Subject-3 : "))

print(f"Marks : {s1},{s2},{s3}")
print(f"Average : {(s1+s2+s3)/3}")
