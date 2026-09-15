'''
Strong Number Checker

A digital lock opens only for strong numbers.

A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.

Input:
145

Output:
Strong Number
'''

n=int(input("Enter The Number : "))
n1=n
sum=0
p=1

while n>0:
    d=n%10
    while d>0:
        p*=d
        d-=1
    sum+=p
    p=1
    n//=10


if sum==n1:
    print("Strong Number")
else:
    print("Not A Strong Number")