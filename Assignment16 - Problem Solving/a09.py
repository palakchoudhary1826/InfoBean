'''
Docstring for Assignment16.a09
Abundant Number Detector

A financial system analyzes surplus numbers.

An Abundant Number:
Sum of proper factors > number

Write a program to check Abundant Number.

Input:
12

Output:
Abundant Number
'''
n=int(input("Enter The Number : "))
sum=1

i=2
while i<n:
    if n%i==0:
        sum+=i
    i+=1

if sum>n:
    print("abundant number")
else:
    print("not abundant number")