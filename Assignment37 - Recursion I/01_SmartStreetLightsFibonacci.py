'''
Assignment 1: Smart Street Lights (Fibonacci Series)

A smart city installs street lights in a newly developed area.
The number of lights installed each month follows the Fibonacci pattern.

Month 1 → 0 lights
Month 2 → 1 light

Every following month, the number of lights installed is the
sum of the previous two months.

Task:
Write a recursive function to print the first N Fibonacci numbers.

Input:
Enter the number of months:
7

Output:
0 1 1 2 3 5 8
'''

def fib(n):
    #base case
    if n==0:
        return 0
    if n==1:
        return 1
    
    
    
    #recursive case
    return fib(n-1)+fib(n-2)

n=int(input("Enter : "))
for i in range(n):
    print(fib(i),end=" ")