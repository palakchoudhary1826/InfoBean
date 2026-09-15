'''
Problem 1: Two Sum

Given an array of integers nums and an integer target, return the
indices of the two numbers such that they add up to target.

You may assume that each input has exactly one solution, and you
may not use the same element twice.

Example 1:
Input:
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]

Example 2:
Input:
nums = [3, 2, 4]
target = 6

Output:
[1, 2]

Example 3:
Input:
nums = [3, 3]
target = 6

Output:
[0, 1]
'''

nums = [2, 7, 11, 15]
target = 10
found=False

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])
            found=True
            break

if not found:
    print(-1)

       
