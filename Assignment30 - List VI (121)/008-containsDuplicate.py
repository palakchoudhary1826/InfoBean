'''
Problem 8: Contains Duplicate

Given an integer array nums, return True if any value appears at
least twice in the array, and return False if every element is
distinct.

Example 1:
Input:
nums = [1, 2, 3, 1]

Output:
True

Explanation:
The value 1 appears more than once.

Example 2:
Input:
nums = [1, 2, 3, 4]

Output:
False

Explanation:
Every element appears only once.

Example 3:
Input:
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

Output:
True
'''

l=list(map(int,input("Enter : ").split()))

s=set(l)

if len(s)!=len(l):
    print("TRUE")
else:
    print("FALSE")