# ============================================================
# 5. Equilibrium Index
# ============================================================
#
# Scenario:
# Find an index where the sum of all elements on the left side
# is equal to the sum of all elements on the right side.
#
# Requirements:
# - Read N and list elements from the user.
# - Find the equilibrium index.
# - If no equilibrium index exists, display an appropriate
#   message.
#
# Note:
# The element at the equilibrium index is not included in
# either the left sum or the right sum.
#
# Test Case 1:
# Input:
# [1, 3, 5, 2, 2]
#
# Output:
# Equilibrium Index = 2
#
# Explanation:
# Left Sum  = 1 + 3 = 4
# Right Sum = 2 + 2 = 4
#
# Test Case 2:
# Input:
# [1, 2, 3]
#
# Output:
# No Equilibrium Index Found
#
# Test Case 3:
# Input:
# [1, 7, 3, 6, 5, 6]
#
# Output:
# Equilibrium Index = 3
#
# Explanation:
# Left Sum  = 1 + 7 + 3 = 11
# Right Sum = 5 + 6 = 11
#
# Test Case 4:
# Input:
# [2, 4, 2]
#
# Output:
# Equilibrium Index = 1
#
# Explanation:
# Left Sum  = 2
# Right Sum = 2
# ============================================================

arr=list(map(int,input("Enter The Elements : ").split(' ')))
print(arr)

n=len(arr)



for i in range(n):
    Lsum=0
    Rsum=0

    for j in range(0,i):
        Lsum+=arr[j]
    
    for j in range(n-1,i,-1):
        Rsum+=arr[j]

    if Lsum==Rsum:
        print(f"Equilibriumm Index at {i}")
    
        break
else:
    print("not found")



