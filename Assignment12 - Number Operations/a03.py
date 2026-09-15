'''
Docstring for a03
Question 3: Perfect Number Reward System

Write a program using a for-else loop to:

Find the sum of proper factors of the given number.
If the sum equals the number, print Reward Unlocked.
Otherwise, print Try Again.

Input

6

Output

Reward Unlocked
'''

n=int(input("Enter The Number : "))
n1=n
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
    if sum==n1:
        print("reward Unlocked")
        break
else : 
    print("Try Again")