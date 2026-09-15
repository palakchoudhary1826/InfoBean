# ============================================================
# 4. Longest Consecutive Sequence
# ============================================================
#
# Scenario:
# Find the longest sequence of consecutive numbers present
# in the list.
#
# Requirements:
# - Read N and list elements from the user.
# - Find the length of the longest consecutive sequence.
# - Display the sequence length.
#
# Note:
# The numbers do not need to be adjacent in the original list.
#
# Test Case 1:
# Input:
# [100, 4, 200, 1, 3, 2]
#
# Output:
# Longest Consecutive Length = 4
#
# Explanation:
# The longest consecutive sequence is:
# 1, 2, 3, 4
#
# Test Case 2:
# Input:
# [10, 11, 12, 20]
#
# Output:
# Longest Consecutive Length = 3
#
# Explanation:
# The longest consecutive sequence is:
# 10, 11, 12
#
# Test Case 3:
# Input:
# [5, 2, 99, 3, 4, 1, 100]
#
# Output:
# Longest Consecutive Length = 4
#
# Explanation:
# The longest consecutive sequence is:
# 1, 2, 3, 4
# ============================================================

arr=list(map(int,input("Enter The Elements : ").split(' ')))
print(arr)

n=len(arr)
arr.sort()
long=1
curr=1
# start=0
# end=0

for i in range(1,n):
    if arr[i]-arr[i-1]==1:
        curr+=1
    else:
        curr=1
        
    if curr>long:
        long=curr
        end=i

print(f"Longest  cons.. length {long}")

for i in range(end - long + 1, end + 1):
    print(arr[i], end=" ")
    
