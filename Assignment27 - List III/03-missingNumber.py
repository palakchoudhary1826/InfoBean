# ============================================================
# 3. Find the Missing Number
# ============================================================
#
# Scenario:
# Numbers from 1 to N should exist in a sequence, but one
# number is missing.
#
# Requirements:
# - Read N and list elements from the user.
# - Find the missing number.
# - Assume the numbers belong to the range 1 to N+1.
#
# Test Case 1:
# Input:
# [1, 2, 3, 5]
#
# Output:
# Missing Number = 4
#
# Test Case 2:
# Input:
# [2, 3, 4, 5]
#
# Output:
# Missing Number = 1
#
# Test Case 3:
# Input:
# [1, 2, 4, 5]
#
# Output:
# Missing Number = 3
# ============================================================
arr=list(map(int,input("Enter The Elements : ").split(' ')))
print(arr)

n=len(arr)
arr.sort()

for i in range(0,n):
    if arr[i]!=i+1:
        print(i+1)
        break