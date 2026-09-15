'''
Docstring for a01
Question 1: Triple Operation Prime Verification System

Write a program to:

Find the sum of digits of the given number.
Reverse the number.
Find the absolute difference between the original and reversed number.
Add the digit sum and the difference.
Check whether the final result is Prime or Not Prime.

Input

4215

Output

Sum of Digits = 12
Reverse = 5124
Difference = 909
Final Result = 921
Not Prime
'''

n=int(input("Enter The Number : "))
n1=n
sum=0
rev=0

while n>0:
    d=n%10
    sum+=d
    rev=rev*10+d
    n//=10

print(f"Sum Of digits : {sum}")
print(f"Reverse of {n1} : {rev}")

diff=abs(n1-rev)
final=diff+sum

print(f"Difference : {diff}")
print(f"final Result :{final}")

n=final
flag=True
if n<=1:
    flag=False
i=2
while i*i<=n:
    if n%i==0:
        flag=False
        break
    i+=1

if flag:
    print("Prime")
else :
    print("Not Prime")