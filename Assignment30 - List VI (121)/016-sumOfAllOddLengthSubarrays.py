'''
Sum of All Odd Length Subarrays

Given an integer array arr, return the sum of all possible odd-length
subarrays of arr.

A subarray is a contiguous part of the array.

An odd-length subarray has a length of 1, 3, 5, 7, etc.

Example 1:
Input:
arr = [1, 4, 2, 5, 3]

Output:
58

Explanation:
The odd-length subarrays are:
[1], [4], [2], [5], [3]
[1, 4, 2], [4, 2, 5], [2, 5, 3]
[1, 4, 2, 5, 3]

Their total sum is 58.

Example 2:
Input:
arr = [1, 2]

Output:
3

Explanation:
The only odd-length subarrays are:
[1], [2]

Their sum is 1 + 2 = 3.

Constraints:
1 <= arr.length <= 100
1 <= arr[i] <= 100
'''


l=list(map(int,input("Enter  : ").split()))
ans=0

for i in range(len(l)):
    sum=0
    for j in range(i,len(l)):
        sum+=l[j]
        check=j-i+1
        if check%2==1:
            ans+=sum

print(ans)
            
