'''
Docstring for Assignment16.a07
Write a program to:

Input a number.
Find the square of the number.
Reverse the number and find its square.
If both squares are reverses of each other, print Adam Number; otherwise, print Not an Adam Number.

Input

12

Output

Adam Number
'''

n=int(input("Enter The Number : "))
sq=n**2
revNum=0

while n>0:
    d=n%10
    revNum=revNum*10+d
    n//=10

SqOfRevNum=revNum**2

revSq=0

while SqOfRevNum>0:
    d=SqOfRevNum%10
    revSq=revSq*10+d
    SqOfRevNum//=10
    



if revSq==sq:
    print("Adam Number")
else:
    print("Not Adam Number")