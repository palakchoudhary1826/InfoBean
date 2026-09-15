'''
Docstring for Assignment16.a04
4.Spy Number Detector

A cybersecurity system flags special numeric codes.

A number is called a Spy Number if:
Sum of digits = Product of digits

Write a program to check whether the entered number is Spy Number or Not.

Input:
1124

Output:
Spy Number
'''

n=int(input("Enter The Number : "))
sum=0
prod=1

while n>0:
    d=n%10
    sum+=d
    prod*=d
    n//=10
print(sum,prod)
if sum==prod:
    print("Spy Number")
else:
    print("not a spy number")