"""
Question 7: Factorial Expansion List

Problem:
    Replace every element with its factorial value and
    perform the required analysis.

Tasks:
    - Convert each element to factorial
    - Find sum
    - Find maximum
    - Count even factorial values

Input:
    A list of integers.

Output:
    Factorial list, Sum, Maximum, Even Count

Test Cases:
    Input :
        [3, 4, 5]
    Output:
        Factorials = [6, 24, 120]
        Sum = 150
        Max = 120
        Even Count = 3
"""

# Write your code below
arr = list(map(int, input("Enter numbers: ").split(" ")))
fact=[]


for i in arr:
    p=1
    for j in range(1,i+1):
        p*=j
    fact.append(p)

print(f"Factorial : {fact}")
print(f"Sum : {sum(fact)}")
print(f"Max : {max(fact)}")

count=0
for i in fact:
    if i%2==0:
        count+=1

print(f"Even Count : {count}")
