'''
Docstring for a02
Question 2: Multi Stage Prime Lock System

Write a program to:

Find the sum of digits.
Find the product of digits.
Find the difference between the product and sum.
Count the digits in the difference.
Add the digit count to the difference.
Check whether the final result is Prime or Not Prime.

Input

234

Output

Sum = 9
Product = 24
Difference = 15
Digits = 2
Final Result = 17
Prime
'''

n=int(input("Enter The Number : "))
n1=n
sum=0
p=1

while n>0:
    d=n%10
    sum+=d
    p*=d
    n//=10

print(f"Sum Of digits : {sum}")
print(f"Product of digits: {p}")

diff=abs(p-sum)
temp=diff
count=0
while diff>0:
    count+=1
    diff//=10

print(f"Difference : {temp}")
print(f"Digits :{count}")
final=temp+count
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