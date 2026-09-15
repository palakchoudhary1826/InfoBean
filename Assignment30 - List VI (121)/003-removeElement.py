'''
Problem 3: Remove Element

Given an integer array nums and an integer val, remove all
occurrences of val in nums in-place.

The order of the elements may be changed.

Return the number of elements in nums which are not equal to val.

Example 1:
Input:
nums = [3, 2, 2, 3]
val = 3

Output:
2

Explanation:
The first two elements of nums should be [2, 2].

Example 2:
Input:
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

Output:
5

Explanation:
The first five elements of nums should be [0, 1, 3, 0, 4].
'''


l=list(map(int,input("Enter The Num : ").split()))
# l=[1,1,2,3,3]
val=int(input("Enter the value : "))
i=0
for j in range(1,len(l)):
    if l[j]!=val:
        l[i]=l[j]
        i+=1


print(l[:i])
print(i)
