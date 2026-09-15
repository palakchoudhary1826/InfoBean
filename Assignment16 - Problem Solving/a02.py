'''
Docstring for Assignment16.a02
Fibonacci Series Generator

Write a program to:

Input n (number of terms).
Print the Fibonacci series up to n terms using a loop.

Input

7

Output

0 1 1 2 3 5 8
'''

n=int(input("Enter The Number : "))

f=0
s=1
sum=0

if n>=1:
    print(f,end=" ")
if n>=2:
    print(s,end=" ")

i=0
while i<n-2:
    sum=f+s
    f=s
    s=sum
    print(sum,end=" ")
    i+=1