'''
Squares of a Sorted Array

Given a sorted integer array nums in non-decreasing order, return an array
containing the squares of each number, also sorted in non-decreasing order.

Examples:

Input:
nums = [-4, -1, 0, 3, 10]

Output:
[0, 1, 9, 16, 100]

Explanation:
The squares are [16, 1, 0, 9, 100].
After sorting them, the result is [0, 1, 9, 16, 100].

Example 2:

Input:
nums = [-7, -3, 2, 3, 11]

Output:
[4, 9, 9, 49, 121]

Constraints:
- The array is sorted in non-decreasing order.
- 1 <= len(nums) <= 10^4
- -10^4 <= nums[i] <= 10^4


'''

l=list(map(int,input("Enter : ").split()))

left=0
right=len(l)-1
ans=[0]*len(l)
pos=len(l)-1

while left<=right:
    if abs(l[left])>abs(l[right]):
       
        ans[pos]=l[left]*l[left]
       
        left+=1


        
    else:
        
        ans[pos]=l[right]*l[right]
        
        right-=1
    
    pos-=1

print(ans)