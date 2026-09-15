'''
Docstring for 03_SecurityPinPalindrome
Assignment 3: Security PIN Verification (Palindrome Number)

A bank allows customers to choose a special PIN. For promotional purposes, the bank rewards customers whose PIN is a palindrome (reads the same from left to right and right to left).

As a software developer, write a recursive program to verify whether the entered PIN is a palindrome.

Task

Write a recursive function to reverse the given number and determine whether it is a palindrome.

Input 1
Enter PIN:
1221
Output 1
Palindrome Number
Input 2
Enter PIN:
1234
Output 2
Not a Palindrome Number
'''
r=0
def rev(n):
    global r
    if n==0:
        return
    
    r=r*10+n%10 
    rev(n//10)

n=int(input("Enter : "))
t=n
rev(n)
print(r==t)

    
