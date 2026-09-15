"""
Question 6: Prime ID Analysis

Problem:
    Extract all prime IDs and perform the required analysis.

Tasks:
    - Extract prime numbers
    - Find sum
    - Find maximum
    - Count prime numbers

Input:
    A list of integers.

Output:
    Prime IDs, Sum, Maximum, Count

Test Cases:
    Input :
        [12, 5, 7, 9, 11, 14, 17]
    Output:
        Prime IDs = [5, 7, 11, 17]
        Sum = 40
        Max = 17
        Count = 4

    Input :
        [4, 6, 8, 10]
    Output:
        Prime IDs = []
        Sum = 0
        Max = -1
        Count = 0
"""

# Write your code below
arr = list(map(int, input("Enter numbers: ").split(",")))
prime=[]

for i in arr:
    if i<=1:
        continue
    else:
        j=2
        while j<=i:
            if i%j==0:
                break
            j+=1
        if j==i:
            prime.append(i)

print(f"Prime IDs : {prime}")
print(f"Sum       :{sum(prime)}")
print(f"Max       :{max(prime)}")
print(f"Count     :{len(prime)}")