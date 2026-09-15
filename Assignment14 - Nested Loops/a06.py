'''
Docstring for Assignment14(Nested Loop).a06
Palindrome Number Range Checker

A barcode verification system checks for palindrome numbers within a specific range.
The user enters starting and ending numbers.
The system displays all palindrome numbers using nested loops.

Input:
Enter starting number: 100
Enter ending number: 200

Output:
Palindrome Numbers are:
101
111
121
131
141
151
161
171
181
191
'''

a=int(input("Enter Starting Number : "))
b=int(input("Enter Ending Number : "))

while a<=b:
    rev=0
    temp=a
    while a>0:
        d=a%10
        rev=rev*10+d
        a//=10

    a=temp
    if a==rev:
        print(a)
    a+=1