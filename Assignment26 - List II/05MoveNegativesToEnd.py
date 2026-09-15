"""
Question 5: Move Negative Elements to End

Problem:
    Move all negative elements to the end of the array
    without changing the relative order of positive
    and negative elements.

Input:
    A list of integers.

Output:
    Rearranged list.

Test Cases:
    Input :
        [1, -1, 3, 2, -7, -5, 11, 6]
    Output:
        [1, 3, 2, 11, 6, -1, -7, -5]

    Input :
        [-5, 7, -3, -4, 9, 10, -1, 11]
    Output:
        [7, 9, 10, 11, -5, -3, -4, -1]
"""

# Write your code below

arr = list(map(int, input("Enter numbers: ").split(",")))

pos=[]
neg=[]

for i in arr:
    if i<0:
        neg.append(i)
    else:
        pos.append(i)

for i in neg:
    pos.append(i)

print(pos)