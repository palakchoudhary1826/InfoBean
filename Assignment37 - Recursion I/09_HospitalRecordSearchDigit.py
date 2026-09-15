'''
Assignment 9: Hospital Record System (Search Digit)

A hospital stores patient IDs as numbers. The administrator wants to verify whether a specific digit exists in a patient ID.

Task:
Write a recursive function to determine whether a given digit is present.

Input:
Enter Patient ID:
5837264

Enter Digit:
7

Output:
Digit Found
'''
found=False

def check(n,a):
    global found
    if n==0:
        return
    
    if n%10==a:
        found=True
        return
    check(n//10,a)

n=int(input("Enter : "))
a=int(input("Enter The Digit : "))

check(n,a)
if found:
    print("digit Found")
else:
    print("no digit found")