'''
Docstring for a06
Question 6: Next Prime Cabin Number Generator

Write a program using loops to:

Find the next prime number greater than the given cabin number.
Print the next available prime cabin number.

Input

24

Output

Next Prime Cabin = 29
'''

n=int(input("Enter The Number : "))
flag=True
ans=0
n1=n+1
while n1<=n*2:
    i=2
    while i*i<=n1:
        if n1%i==0:
            flag=False
            break
        i+=1
    if flag:
        ans=n1
        break
    else:
        n1+=1
        flag=True

print(f"Next Prime Cabin : {ans}")