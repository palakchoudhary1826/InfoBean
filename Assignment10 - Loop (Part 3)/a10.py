'''
Prime Security Code Checker

A high-security research lab uses numeric passcodes to unlock restricted doors. To improve security,
 only prime numbers are accepted because they have exactly two factors and are harder to predict using common patterns.

When an employee enters a code, the system must verify whether the number is prime. If yes, access is granted; otherwise, access is denied.

Write a program to check whether the entered number is Prime or Not Prime.

Input:
29

Output:
Prime Number
'''

n=int(input("Enter The Number :"))
flag=False

if n<=1:
    flag=True
i=2
while i*i<=n:
    if n%i==0:
        flag=True
        break
    i+=1

print("Not Prime" if flag else "Prime") 