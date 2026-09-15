'''
Docstring for Assignment18.a05
Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45

Output: Secure Password
'''


n=input("Enter The Password : ")
upper=0
digit=0
count=0
special=0
space=0
i=0
if n[0]>="A" and n[0]<="Z":
    upper=1

if n[len(n)-1]>="0" and n[len(n)-1]<="9":
    digit=1

while i<len(n):

    if n[i]>="0" and n[i]<="9":
        count+=1

    if n[i] in "@#$%&*":
        special=1

    if n[i]==" ":
        space=1

    i+=1

if upper==1 and digit==1 and count>=2 and special==1 and space==0 and (len(n)>=8 and len(n)<=15):
    print("Secure Password")
else:
    print("Invalid Password")



