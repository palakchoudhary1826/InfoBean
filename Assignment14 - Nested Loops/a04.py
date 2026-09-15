'''

Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407
'''

a=int(input("Enter Starting Number : "))
b=int(input("Enter Ending Number : "))

while a<=b:
    temp=a
    sum=0
    p=len(str(a))
    if p>1:
        while a>0:
            d=a%10
            sum+=(d**p)
            a//=10
        a=temp    

    if a==sum:
        print(a)
    a+=1
