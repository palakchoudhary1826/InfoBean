"""
Find the Difference of Two Arrays

Given two integer arrays nums1 and nums2, return two lists:

1. All distinct integers in nums1 that are not present in nums2.
2. All distinct integers in nums2 that are not present in nums1.

The order of the elements in the returned lists does not matter.

Example:
Input: nums1 = [1, 2, 3], nums2 = [2, 4, 6]

Output: [[1, 3], [4, 6]]

Example 2:
Input:
nums1 = [1, 2, 3, 3]
nums2 = [1, 1, 2, 2]

Output:
[[3], []]

Example 3:
Input:
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

Output:
[[1, 2, 3], [4, 5, 6]]

Example 4:
Input:
nums1 = [1, 2, 3]
nums2 = [1, 2, 3]

Output:
[[], []]
"""

num1=list(map(int,input("Enter 1st : ").split()))
num2=list(map(int,input("Enter 2st : ").split()))

set1=set(num1)
set2=set(num2)

a1=set1-set2
a2=set2-set1
# print(set1,set2)
ans=[list(a1),list(a2)]
print(ans)