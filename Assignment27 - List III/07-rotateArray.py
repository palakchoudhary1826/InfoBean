# ============================================================
# 7. Rotate Array K Times to the Right
# ============================================================
#
# Scenario:
# Rotate the array K times towards the right.
#
# Requirements:
# - Read N and list elements from the user.
# - Read K, the number of rotations.
# - Rotate the array K times towards the right.
# - Display the rotated array.
#
# Test Case 1:
# Input:
# Array = [1, 2, 3, 4, 5]
# K = 2
#
# Output:
# [4, 5, 1, 2, 3]
#
# Test Case 2:
# Input:
# Array = [10, 20, 30, 40]
# K = 1
#
# Output:
# [40, 10, 20, 30]
#
# Test Case 3:
# Input:
# Array = [1, 2, 3, 4, 5, 6]
# K = 3
#
# Output:
# [4, 5, 6, 1, 2, 3]
#
# Test Case 4:
# Input:
# Array = [7, 8, 9]
# K = 5
#
# Output:
# [8, 9, 7]
#
# Explanation:
# 5 % 3 = 2, so rotating 5 times is the same as
# rotating the array 2 times.
#
# ============================================================
arr=list(map(int,input("Enter The Elements : ").split(' ')))
k=int(input("Enter The Number Of Rotation : "))
print(arr)


n=len(arr)
k=k%n
arr1=[]

for i in range(n-k,n):
    arr1.append(arr[i])

print(arr1)
for i in range(0,n-k):
    arr1.append(arr[i])

print(arr1)
