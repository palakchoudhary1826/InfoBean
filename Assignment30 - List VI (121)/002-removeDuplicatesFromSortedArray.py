'''
Problem 2: Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove
the duplicates in-place such that each unique element appears only
once.

The relative order of the elements should be kept the same.

Return the number of unique elements in nums.

Example 1:
Input:
nums = [1, 1, 2]

Output:
2

Explanation:
The first two elements of nums should be [1, 2].

Example 2:
Input:
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

Output:
5

Explanation:
The first five elements of nums should be [0, 1, 2, 3, 4].
'''

# l=list(map(int,input("Enter The Num : ").split()))
l=[1,1,2,3,3]

i=0 #i pointer
for j in range(1,len(l)):  #j pointer
    if l[j]!=l[i]:
        i+=1
        l[i]=l[j] #swap 

print(l)
print(l[:i + 1])
print(i+1)