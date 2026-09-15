'''
Assignment 8: Cyber Security (Strong Password Check)

A cybersecurity company considers a numeric password to be "strong" if every digit is even.

Task:
Write a recursive function to check whether all digits of the given number are even.

Input 1:
Enter Password:
248620

Output 1:
Strong Password

Input 2:
Enter Password:
248621

Output 2:
Weak Password
'''
eve=True
def check(n):
    global eve
    if n==0:
        return
    if (n%10)%2!=0:
        eve=False
        return
    
    
    check(n//10)

n=int(input("Enter : "))
check(n)

if eve:
    print("Strong Number")
else:
    print("Weak Number")