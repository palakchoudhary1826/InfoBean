'''
Step Difference Number Analyzer

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number

Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number
'''
n=int(input("Enter The Number : "))
l=len(str(n))
last=n%10
n//=10
step=0

while n>0:
    secondLast=n%10
    diff=secondLast-last if secondLast>last else last-secondLast
    step=step*10+diff
    last=secondLast
    n//=10

stepRev=0
sum=0
max=0

while step>0:
    d=step%10
    sum+=d
    max=d if d>max else max
    stepRev=stepRev*10+d
    
    step//=10

print(f"Step Difference : {stepRev}")
print(f"sum : {sum}")
print(f"max : {max}")

if sum%l==0:
    print("Balanced Number")
else:
    print("Unbalanced Number")


