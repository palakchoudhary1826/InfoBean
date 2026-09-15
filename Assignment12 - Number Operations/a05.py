'''
Docstring for a05
Question 5: Number Stability Analyzer

Write a program using a for-else loop to:

Check whether every next digit is greater than the previous digit.
If true, print Stable Number.
Otherwise, print Unstable Number.

Input

12359

Output

Stable Number
'''
n=int(input("Enter The Number : "))
last=n%10
n//=10
l=len(str(n))
for i in range(1,l):
    d=n%10
    if d>=last:
        print("not stable")
        break
    last=d
    n//=10
else:
    print("stable")
