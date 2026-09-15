"""
Question 4: Sum of Leaders After Filtering Invalid Data

Problem:
    Remove all negative numbers and zeros.
    Find all leader elements from the filtered array.
    Return the sum of all leader elements.

Input:
    n
    n space-separated integers

Output:
    Sum of valid leaders.
    Return -1 if no positive elements exist.

Test Cases:
    Input:
        8
        16 0 17 4 -3 3 5 2
    Output:
        24

    Input:
        6
        -1 0 -5 0 -2 -3
    Output:
        -1

    Input:
        5
        10 20 30 40 50
    Output:
        50
"""

# Write your code below
arr = list(map(int, input("Enter numbers: ").split(",")))

valid=[]
invalid=[]

for i in arr :
    if i<=0:
        invalid.append(i)
    else:
        valid.append(i)

if valid:
    lead=[]
    max=valid[-1]
    lead.append(max)

    for i in range(len(valid)-2,-1,-1):
        if valid[i]>max:
            max=valid[i]
            lead.append(max)

    print(f"Leader Are :{lead}")
    print(f"Sum Of Leader : {sum(lead)}")
else:
    print("-1 for no valid")