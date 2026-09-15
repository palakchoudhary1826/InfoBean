# ============================================================
# 10. Find Duplicate Numbers
# ============================================================
#
# Scenario:
#
# A company stores employee IDs in a list. Some IDs may appear
# more than once due to data entry errors.
#
# Requirements:
#
# - Read N and list elements from the user.
# - Find all duplicate numbers.
# - Store duplicate numbers in another list.
# - Count the total number of duplicate numbers.
# - Display duplicates in sorted order.
#
# Note:
#
# Each duplicate number should be stored only once in the
# duplicate list, even if it appears more than two times.
#
# Test Case 1:
#
# Input:
# [1, 2, 3, 2, 4, 5, 1]
#
# Output:
# Duplicate Numbers = [1, 2]
# Count = 2
#
# Explanation:
#
# 1 appears 2 times.
# 2 appears 2 times.
#
# Therefore:
# Duplicate Numbers = [1, 2]
#
# Test Case 2:
#
# Input:
# [10, 20, 30]
#
# Output:
# No Duplicate Numbers Found
#
# Test Case 3:
#
# Input:
# [5, 5, 5, 2, 3, 3, 7]
#
# Output:
# Duplicate Numbers = [3, 5]
# Count = 2
#
# Explanation:
#
# 5 appears 3 times.
# 3 appears 2 times.
#
# Each duplicate number is stored only once.
#
# Test Case 4:
#
# Input:
# [4, 1, 4, 2, 1, 4, 3]
#
# Output:
# Duplicate Numbers = [1, 4]
# Count = 2
#
# ============================================================

arr=list(map(int,input("Enter The Elements : ").split(' ')))

print(arr)

result=[]


for i in arr:
    count=0
    for j in arr:
        if i==j:
            count+=1
    
    if count>=2 and i not in result:
        result.append(i)
        

result.sort()
if len(result)!=0:
    print(f"Duplicates ID : {result}")
    print(f"Count of Duplicate :{len(result)}")
else:
    print("No Duplicate IDs Found")



