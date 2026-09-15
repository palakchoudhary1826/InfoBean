'''
Docstring for Assignment14(Nested Loop).a05
Strong Number Detector

A banking security system uses Strong Numbers for special authentication testing.
The user enters a range of numbers.
The system identifies all Strong Numbers between the given range using nested loops.

A Strong Number is a number in which the sum of factorials of its digits is equal to the original number.

Example:
145

1! + 4! + 5!
= 1 + 24 + 120
= 145

Since the sum is equal to the original number, 145 is called a Strong Number.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Strong Numbers are:
1
2
145
'''
a=int(input("Enter Starting Number : "))
b=int(input("Enter Ending Number : "))

while a<=b:
    temp=a
    sum=0
    
    while a>0:
        p=1
        d=a%10
        i=1
        while i<=d:
            p*=i
            i+=1
        sum+=p
        a//=10
    a=temp
    if sum==a:
        print(a)
    
    a+=1

        


        