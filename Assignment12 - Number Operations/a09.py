'''
Docstring for a09
Question 9: Bike Service Kilometer Checker

Write a program to:

Read the travelled kilometers.
Print every 3000 km service checkpoint up to the entered distance.

Input

10000

Output

3000 6000 9000
'''
n=int(input("Enter The Distance : "))
checkpoint=0

while n>=3000:
    checkpoint+=3000
    print(checkpoint,end=" ")
    n-=3000
