'''
Problem 13: Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range
[1, n], return all the integers in the range [1, n] that do not
appear in nums.

Example 1:
Input:
nums = [4, 3, 2, 7, 8, 2, 3, 1]

Output:
[5, 6]

Explanation:
The numbers from 1 to 8 are:
[1, 2, 3, 4, 5, 6, 7, 8]

Numbers 5 and 6 do not appear in the array.

Example 2:
Input:
nums = [1, 1]

Output:
[2]

Constraints:
- n == nums.length
- 1 <= n <= 10^5
- 1 <= nums[i] <= n
'''

l=list(map(int,input("Enter : ").split()))


miss=[]
l=sorted(set(l))

for i in range(len(l)):
    if l[i]!=i+1:
        miss.append(i+1)

print(miss)