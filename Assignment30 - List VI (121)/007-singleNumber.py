'''
Problem 7: Single Number

Given a non-empty array of integers nums, every element appears
twice except for one element that appears only once.

Find and return the element that appears only once.

You must implement a solution with linear runtime complexity and
use only constant extra space.

Example 1:
Input:
nums = [2, 2, 1]

Output:
1

Example 2:
Input:
nums = [4, 1, 2, 1, 2]

Output:
4

Example 3:
Input:
nums = [1]

Output:
1
'''

l=list(map(int,input("Enter :").split()))
ans=0
for i in l:
    ans^=i #XOR same = 0 diff =1 

print(ans)


