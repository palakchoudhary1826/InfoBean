'''
Problem 4: Search Insert Position

Given a sorted array of distinct integers and a target value,
return the index if the target is found.

If the target is not found, return the index where it would be
inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input:
nums = [1, 3, 5, 6]
target = 5

Output:
2

Example 2:
Input:
nums = [1, 3, 5, 6]
target = 2

Output:
1

Example 3:
Input:
nums = [1, 3, 5, 6]
target = 7

Output:
4

Example 4:
Input:
nums = [1, 3, 5, 6]
target = 0

Output:
0
'''


l=list(map(int,input("Enter The element in Sorted way : ").split()))
target=int(input("Enter The Target : "))

low=0
high=len(l)-1


while low<=high:
    mid=low+(high-low)//2

    if l[mid]==target:
        print(f"index at : {mid}")
        break

    elif target>l[mid]:
        low=mid+1
    else:
        high=mid-1
else:
    print(f"Index At : {low} ")

