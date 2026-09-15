'''
Docstring for Assignment14(Nested Loop).a03
Prime Number Range Checker

A cyber security system generates prime numbers for encryption analysis.
The user enters a starting number and ending number.
The system checks and displays all prime numbers between the given range using nested loops.

Input:
Enter starting number: 10
Enter ending number: 50

Output:
Prime Numbers are:
11
13
17
19
23
29
31
37
41
43
47
'''

a=int(input("Enter Starting Number : "))
b=int(input("Enter Ending Number : "))
print("Prime Number Are : ")

while a<=b:
    if a<=1:
        a+=1
        continue
    
    else:
        i=2
        while i*i<=a:
            if a%i==0:
                break
            i+=1
        else:

            print(a)
        a+=1