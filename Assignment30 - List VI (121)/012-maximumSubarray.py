'''
Problem 12: Maximum Subarray

Given an integer array nums, find the subarray with the largest sum,
and return its sum.

A subarray is a contiguous part of an array.

Example 1:
Input:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Output:
6

Explanation:
The subarray [4, -1, 2, 1] has the largest sum.
Sum = 4 + (-1) + 2 + 1 = 6.

Example 2:
Input:
nums = [1]

Output:
1

Example 3:
Input:
nums = [5, 4, -1, 7, 8]

Output:
23

Explanation:
The subarray [5, 4, -1, 7, 8] has the largest sum.

Constraints:
- A subarray must contain at least one element.
- The subarray must contain consecutive elements.
'''

l=[5, 4, -1, 7, 8]
maxsum=0
for i in range(len(l)):
    sum=0
    for j in range(i,len(l)):
        sum+=l[j]
        # print(sum)
        if sum>maxsum:
            maxsum=sum

print(maxsum)