'''

 Display Numbers Ending with 5

A supermarket tracks token numbers ending in 5.
Write a program using loops to display numbers ending with 5 between two numbers.

Input:
10 40

Output:
15 25 35
'''
n1=int(input("Enter The 1st Number: "))
n2=int(input("Enter The 2st Number: "))

# while n1<=n2:
#     if n1%5==0:
#         d=n1%10
#         if d==5:
#             print(n1,end=" ")
#     n1+=1

while n1<=n2:
    d=n1%10
    if d==5:
        print(n1,end=" ")
    n1+=1
    