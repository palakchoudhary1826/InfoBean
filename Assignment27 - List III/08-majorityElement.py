# ============================================================
# 8. Majority Element
# ============================================================
#
# Scenario:
# Find an element that occurs more than N/2 times in the list.
#
# Requirements:
# - Read N and list elements from the user.
# - Find the majority element.
# - If no majority element exists, display an appropriate
#   message.
#
# Note:
# A majority element must occur strictly more than N/2 times.
#
# Test Case 1:
# Input:
# [2, 2, 1, 2, 3, 2, 2]
#
# Output:
# Majority Element = 2
#
# Explanation:
# N = 7
# N/2 = 3.5
# 2 occurs 5 times.
# Since 5 > 3.5, 2 is the majority element.
#
# Test Case 2:
# Input:
# [1, 2, 3, 4]
#
# Output:
# No Majority Element Found
#
# Explanation:
# N = 4
# N/2 = 2
# No element occurs more than 2 times.
#
# Test Case 3:
# Input:
# [3, 3, 4, 2, 3, 3]
#
# Output:
# Majority Element = 3
#
# Explanation:
# N = 6
# N/2 = 3
# 3 occurs 4 times.
# Since 4 > 3, 3 is the majority element.
#
# Test Case 4:
# Input:
# [1, 1, 2, 2, 2]
#
# Output:
# Majority Element = 2
#
# Explanation:
# N = 5
# N/2 = 2.5
# 2 occurs 3 times.
# Since 3 > 2.5, 2 is the majority element.
#
# ============================================================

arr=list(map(int,input("Enter The Elements : ").split(' ')))

print(arr)

found=False

n=len(arr)
N=n/2


for i in arr:
    count=0
    for j in arr:
        if i==j:
            count+=1
    
    if count>N:
        digit=i
        found=True

if found!=True:
    print("No majority element ")
else:
    print("Found")
    print(digit)

