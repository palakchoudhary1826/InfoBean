"""
Question 1: Mountain Hiking Elevation Analysis

Problem:
    Given an array of elevations, find the index of any one peak element.
    A peak element is greater than or equal to its adjacent elements.

Input:
    A list of integers.

Output:
    Index of any one peak element.

Test Cases:
    Input : [1200, 1450, 1700, 1600, 1500]
    Output: 2

    Input : [800, 900, 950, 1000]
    Output: 3

    Input : [3000]
    Output: 0
"""

arr = list(map(int, input("Enter numbers: ").split(",")))

print(arr)

n=len(arr)


for i in range(n):

    if i==0:
        if n==1 or arr[i]>=arr[i+1]:
            print(f"Peak Element {arr[i]} at index  {i}")
            break
    elif i==n-1:
        if arr[i]>=arr[i-1]:
            print(f"Peak Element {arr[i]} at index  {i}")
            break
    else:
        if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
            print(f"Peak Element {arr[i]} at index  {i}")
            break
