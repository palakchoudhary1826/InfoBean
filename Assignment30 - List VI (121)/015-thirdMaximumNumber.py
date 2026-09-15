"""
Third Maximum Number

Given an integer array nums, return the third distinct maximum number
in the array.

If the third maximum number does not exist, return the maximum number.

Note:
The third maximum number must be distinct.

Examples:

Example 1:
Input:
nums = [3, 2, 1]

Output:
1

Explanation:
The maximum number is 3.
The second maximum number is 2.
The third maximum number is 1.

Example 2:
Input:
nums = [1, 2]

Output:
2

Explanation:
There is no third distinct maximum number,
so return the maximum number 2.

Example 3:
Input:
nums = [2, 2, 3, 1]

Output:
1

Explanation:
The distinct numbers are [1, 2, 3].
The third maximum number is 1.

Example 4:
Input:
nums = [5, 5, 4, 3, 2, 1]

Output:
3

Explanation:
The distinct maximum numbers are:
5 → first maximum
4 → second maximum
3 → third maximum
"""

l = list(map(int, input("Enter :").split()))
# l2=list(set(l))
# print(l2)
firstMax = 0 #pehle
secondMax = 0 # second
thirdMax = 0
# [3,2,1]
for i in l:

    if i==firstMax or i==secondMax or i==thirdMax:
        continue

    
    if i > firstMax:
        thirdMax=secondMax
        secondMax=firstMax
        firstMax = i  # 3

    if i < firstMax and i > secondMax: 
        thirdMax=secondMax
        secondMax = i

    if i > thirdMax:
        thirdMax = i


# print(firstMax,secondMax,thirdMax)

if not thirdMax:
    print(firstMax)
else:
    print(thirdMax)