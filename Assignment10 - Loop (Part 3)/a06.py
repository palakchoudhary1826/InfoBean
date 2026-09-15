'''

Automorphic Number Checker

A digital security company designs smart lockers that open only for special self-matching numeric codes. When a user enters a number, the system squares the number and checks whether the result ends with the same digits as the original code. If yes, the locker grants access.

An automorphic number is a number whose square ends with the same number.

Example:
25² = 625

Write a program using loops to check whether the entered number is an Automorphic number.

Input:
25

Output:
Automorphic Number
'''
n=int(input("Enter The Number : "))
sq=n**2
sum=0
l=len(str(n))

while l>0:
    d=sq%10
    sum=(sum*10)+d
    sq//=10
    l-=1
print(sum)
sum1=0
#reverse
while sum>0:
    d=sum%10
    sum1=(sum1*10)+d
    sum//=10

if sum1==n:
    print("automorphic")
else:
    print("not automorphic")




    
