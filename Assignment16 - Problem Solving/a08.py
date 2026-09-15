'''
Docstring for Assignment16.a08
Trimorphic Number Analyzer

A coding system checks cube-based patterns.

A Trimorphic Number:
Cube of number ends with the same number.

Example:
4³ = 64

Write a program to check Trimorphic Number.

Input:
4

Output:
Trimorphic Number
'''

n=int(input("Enter The Number : "))
l=len(str(n))
cb=n**3
# print(cb)
last=cb%(10**l)
# print(last)
if last==n:
    print("Trimorphic Number")
else:
    print("not Trimorphic number")

