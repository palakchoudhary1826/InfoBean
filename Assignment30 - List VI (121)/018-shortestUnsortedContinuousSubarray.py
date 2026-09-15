'''
Shortest Unsorted Continuous Subarray

Given an integer array nums, find the shortest continuous subarray
that, if you sort it in ascending order, makes the entire array
sorted in ascending order.

Return the length of the shortest such subarray.

Example 1:

Input:
nums = [2, 6, 4, 8, 10, 9, 15]

Output:
5

Explanation:
The subarray [6, 4, 8, 10, 9] is the shortest subarray that needs
to be sorted.

After sorting it:
[2, 4, 6, 8, 9, 10, 15]

Example 2:

Input:
nums = [1, 2, 3, 4]

Output:
0

Explanation:
The array is already sorted.

Example 3:

Input:
nums = [1]

Output:
0

Constraints:
1 <= len(nums) <= 10^4
-10^5 <= nums[i] <= 10^5
'''

l=list(map(int,input("Enter ").split()))