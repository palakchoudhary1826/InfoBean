'''
Assignment 10: Mobile Recharge System

A telecom company issues lucky recharge coupons only if the coupon number is prime.

Task:
Write a recursive function to determine whether a given number is prime.

Input:
Enter Coupon Number:
29

Output:
Prime Number
'''

def check_prime(n,i):
    if n<=1:
        return False
    
    if i>n//2:
        return True
    
    if n%i==0:
        return False
    
    return check_prime(n,i+1)

n=int(input("Enter : "))

ans=check_prime(n,2)
if ans:
    print("Prime Number")
else:
    print("Not Prime Number")

