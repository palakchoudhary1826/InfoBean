'''
1. Product of Odd Numbers up to N

A puzzle game rewards players by multiplying odd numbers up to n.
Write a program using loops to find product of odd numbers.

Input:
5

Output:
15
'''
n=int(input("Enter The Number : "))

p=1
i=1
while i<=n:
    if i%2!=0:
        p*=i
    i+=1
    
print(p)