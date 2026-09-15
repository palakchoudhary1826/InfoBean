# ============================================================
# 6. Product of Array Except Self
# ============================================================
#
# Scenario:
# For every element, calculate the product of all other
# elements except itself.
#
# Requirements:
# - Read N and list elements from the user.
# - Create a new list containing the products.
# - Display the result.
#
# Note:
# The current element must not be included in its own product.
#
# Test Case 1:
# Input:
# [1, 2, 3, 4]
#
# Output:
# [24, 12, 8, 6]
#
# Explanation:
# 1 → 2 × 3 × 4 = 24
# 2 → 1 × 3 × 4 = 12
# 3 → 1 × 2 × 4 = 8
# 4 → 1 × 2 × 3 = 6
#
# Test Case 2:
# Input:
# [2, 3, 5]
#
# Output:
# [15, 10, 6]
#
# Explanation:
# 2 → 3 × 5 = 15
# 3 → 2 × 5 = 10
# 5 → 2 × 3 = 6
#
# Test Case 3:
# Input:
# [1, 2, 3, 4, 5]
#
# Output:
# [120, 60, 40, 30, 24]
#
# Test Case 4:
# Input:
# [2, 4, 6]
#
# Output:
# [24, 12, 8]
# ============================================================


arr=list(map(int,input("Enter The Elements : ").split(' ')))
print(arr)
n=len(arr)

result=[]


for i in range(n):
    p=1
    for j in range(n):
        if i==j:
            continue
        else:
            p*=arr[j]
    
    result.append(p)

print(result)




